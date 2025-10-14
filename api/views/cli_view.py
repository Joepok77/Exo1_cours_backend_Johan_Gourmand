from typing import List
from models.task import Task, TaskStatus


class CLIView:

    @staticmethod
    def display_menu():
        print("\n" + "=" * 50)
        print("      TODOLIST - GESTIONNAIRE DE TACHES")
        print("=" * 50)
        print("1. Ajouter une tache")
        print("2. Afficher toutes les taches")
        print("3. Supprimer une tache")
        print("4. Quitter")
        print("=" * 50)

    @staticmethod
    def display_tasks(tasks: List[Task], title: str = "Liste des tâches"):
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
        print("\n--- Détails de la tâche ---")
        print(f"ID: {task.id}")
        print(f"Titre: {task.title}")
        print(f"Description: {task.description or 'Aucune description'}")
        print(f"Statut: {task.status.value}")
        print(f"Créée le: {task.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Modifiée le: {task.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")

    @staticmethod
    def get_input(prompt: str) -> str:
        return input(f"\n{prompt}: ").strip()

    @staticmethod
    def display_success(message: str):
        print(f"\n[OK] {message}")

    @staticmethod
    def display_error(message: str):
        print(f"\n[ERREUR] {message}")

    @staticmethod
    def display_info(message: str):
        print(f"\n[INFO] {message}")

    @staticmethod
    def display_status_menu():
        print("\nChoisissez un statut:")
        print("1. À faire")
        print("2. En cours")
        print("3. Terminé")

    @staticmethod
    def clear_screen():
        print("\n" * 2)
