"""
Modèle Task - Représente une tâche dans la ToDoList
"""
from datetime import datetime
from enum import Enum


class TaskStatus(Enum):
    """Énumération des statuts possibles d'une tâche"""
    TODO = "À faire"
    IN_PROGRESS = "En cours"
    DONE = "Terminé"


class Task:
    """Classe représentant une tâche"""

    _id_counter = 1

    def __init__(self, title: str, description: str = "", status: TaskStatus = TaskStatus.TODO):
        """
        Initialise une nouvelle tâche

        Args:
            title: Le titre de la tâche
            description: La description de la tâche (optionnel)
            status: Le statut de la tâche (par défaut: TODO)
        """
        self.id = Task._id_counter
        Task._id_counter += 1
        self.title = title
        self.description = description
        self.status = status
        """ self.created_at = datetime.now() """
        """ self.updated_at = datetime.now() """

    def update_status(self, new_status: TaskStatus):
        """Met à jour le statut de la tâche"""
        self.status = new_status
        self.updated_at = datetime.now()

    def update_info(self, title: str = None, description: str = None):
        """Met à jour les informations de la tâche"""
        if title:
            self.title = title
        if description is not None:
            self.description = description
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """Convertit la tâche en dictionnaire"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status.value,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    def __str__(self) -> str:
        """Représentation string de la tâche"""
        return f"[{self.id}] {self.title} - {self.status.value}"

    def __repr__(self) -> str:
        """Représentation détaillée de la tâche"""
        return f"Task(id={self.id}, title='{self.title}', status={self.status.value})"
