"""
TaskController - Gère la logique métier des tâches
"""
from typing import List, Optional
from datetime import datetime
from models.task import Task, TaskStatus
from utils.storage import StorageManager


class TaskController:
    """Contrôleur pour gérer les opérations sur les tâches"""

    def __init__(self):
        """Initialise le contrôleur avec une liste vide de tâches"""
        self.tasks: List[Task] = []
        self.storage = StorageManager()
        self._load_tasks()

    def _load_tasks(self):
        """Charge les tâches depuis le fichier JSON au démarrage"""
        tasks_data = self.storage.load_tasks()

        for task_dict in tasks_data:
            task = Task(task_dict['title'], task_dict['description'])
            task.id = task_dict['id']

            # Restaurer le statut
            for status in TaskStatus:
                if status.value == task_dict['status']:
                    task.status = status
                    break

            # Restaurer les dates
            task.created_at = datetime.strptime(task_dict['created_at'], '%Y-%m-%d %H:%M:%S')
            task.updated_at = datetime.strptime(task_dict['updated_at'], '%Y-%m-%d %H:%M:%S')

            self.tasks.append(task)

        # Mettre à jour le compteur d'ID
        if self.tasks:
            Task._id_counter = max(task.id for task in self.tasks) + 1

    def _save_tasks(self):
        """Sauvegarde les tâches dans le fichier JSON"""
        self.storage.save_tasks(self.tasks)

    def create_task(self, title: str, description: str = "") -> Task:
        """
        Crée une nouvelle tâche

        Args:
            title: Le titre de la tâche
            description: La description de la tâche

        Returns:
            La tâche créée
        """
        task = Task(title, description)
        self.tasks.append(task)
        self._save_tasks()  # Sauvegarde automatique
        return task

    def get_all_tasks(self) -> List[Task]:
        """Retourne toutes les tâches"""
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Récupère une tâche par son ID

        Args:
            task_id: L'ID de la tâche

        Returns:
            La tâche ou None si non trouvée
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: str = None, description: str = None) -> bool:
        """
        Met à jour une tâche

        Args:
            task_id: L'ID de la tâche
            title: Nouveau titre (optionnel)
            description: Nouvelle description (optionnel)

        Returns:
            True si la mise à jour a réussi, False sinon
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.update_info(title, description)
            self._save_tasks()  # Sauvegarde automatique
            return True
        return False

    def update_task_status(self, task_id: int, status: TaskStatus) -> bool:
        """
        Met à jour le statut d'une tâche

        Args:
            task_id: L'ID de la tâche
            status: Le nouveau statut

        Returns:
            True si la mise à jour a réussi, False sinon
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.update_status(status)
            self._save_tasks()  # Sauvegarde automatique
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Supprime une tâche

        Args:
            task_id: L'ID de la tâche

        Returns:
            True si la suppression a réussi, False sinon
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self._save_tasks()  # Sauvegarde automatique
            return True
        return False

    def get_tasks_by_status(self, status: TaskStatus) -> List[Task]:
        """
        Filtre les tâches par statut

        Args:
            status: Le statut à filtrer

        Returns:
            Liste des tâches avec ce statut
        """
        return [task for task in self.tasks if task.status == status]

    def get_task_count(self) -> int:
        """Retourne le nombre total de tâches"""
        return len(self.tasks)
