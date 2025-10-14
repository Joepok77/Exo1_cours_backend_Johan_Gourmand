"""
CLIView - Gère l'interface en ligne de commande
"""
from typing import List
from models.task import Task, TaskStatus


class CLIView:
    """Vue pour l'interface CLI de la ToDoList"""

    @staticmethod
    def display_menu():
        """Affiche le menu principal"""
        print("\n" + "=" * 50)
        print("      TODOLIST - GESTIONNAIRE DE TACHES")
        print("=" * 50)
        print("1. Ajouter une tache")
        print("2. Afficher toutes les taches")
        print("3. Afficher les taches par statut")
        print("4. Modifier une tache")
        print("5. Changer le statut d'une tache") 
        print("6. Supprimer une tache")
        print("7. Quitter")
        print("=" * 50)

    @staticmethod
    def display_tasks(tasks: List[Task], title: str = "Liste des tâches"):
        """
        Affiche une liste de tâches

        Args:
            tasks: Liste des tâches à afficher
            title: Titre de la section
        """
        print(f"\n--- {title} ---")
        if not tasks:
            print("Aucune tâche trouvée.")
            return

        for task in tasks:
            status_icon = "[OK]" if task.status == TaskStatus.DONE else "[~]" if task.status == TaskStatus.IN_PROGRESS else "[ ]"
            print(f"{status_icon} {task}")
            if task.description:
                print(f"   Description: {task.description}")
            print(f"   Créée le: {task.created_at.strftime('%Y-%m-%d %H:%M')}")
            print()

    @staticmethod
    def display_task_details(task: Task):
        """
        Affiche les détails d'une tâche

        Args:
            task: La tâche à afficher
        """
        print("\n--- Détails de la tâche ---")
        print(f"ID: {task.id}")
        print(f"Titre: {task.title}")
        print(f"Description: {task.description or 'Aucune description'}")
        print(f"Statut: {task.status.value}")
        print(f"Créée le: {task.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Modifiée le: {task.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")

    @staticmethod
    def get_input(prompt: str) -> str:
        """
        Demande une saisie utilisateur

        Args:
            prompt: Le message à afficher

        Returns:
            La saisie de l'utilisateur
        """
        return input(f"\n{prompt}: ").strip()

    @staticmethod
    def display_success(message: str):
        """Affiche un message de succès"""
        print(f"\n[OK] {message}")

    @staticmethod
    def display_error(message: str):
        """Affiche un message d'erreur"""
        print(f"\n[ERREUR] {message}")

    @staticmethod
    def display_info(message: str):
        """Affiche un message d'information"""
        print(f"\n[INFO] {message}")

    @staticmethod
    def display_status_menu():
        """Affiche le menu de sélection de statut"""
        print("\nChoisissez un statut:")
        print("1. À faire")
        print("2. En cours")
        print("3. Terminé")

    @staticmethod
    def clear_screen():
        """Efface l'écran (simulation)"""
        print("\n" * 2)
