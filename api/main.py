"""
Point d'entrée de l'application ToDoList CLI
"""
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent))

from controllers.task_controller import TaskController
from views.cli_view import CLIView
from models.task import TaskStatus


class ToDoListApp:
    """Application principale de gestion de taches"""

    def __init__(self):
        """Initialise l'application"""
        self.controller = TaskController()
        self.view = CLIView()
        self.running = True

    def run(self):
        """Lance l'application"""
        self.view.display_info("Bienvenue dans votre gestionnaire de taches!")

        while self.running:
            try:
                self.view.display_menu()
                choice = self.view.get_input("Choisissez une option (1-7)")

                if choice == "1":
                    self.add_task()
                elif choice == "2":
                    self.display_all_tasks()
                elif choice == "3":
                    self.display_tasks_by_status()
                elif choice == "4":
                    self.update_task()
                elif choice == "5":
                    self.change_task_status()
                elif choice == "6":
                    self.delete_task()
                elif choice == "7":
                    self.quit_app()
                else:
                    self.view.display_error("Option invalide. Choisissez entre 1 et 7.")

            except KeyboardInterrupt:
                print("\n")
                self.quit_app()
            except Exception as e:
                self.view.display_error(f"Une erreur est survenue: {str(e)}")

    def add_task(self):
        """Ajoute une nouvelle tache"""
        title = self.view.get_input("Titre de la tache")
        if not title:
            self.view.display_error("Le titre ne peut pas etre vide.")
            return

        description = self.view.get_input("Description (optionnel)")

        task = self.controller.create_task(title, description)
        self.view.display_success(f"Tache créée avec succés! (ID: {task.id})")

    def display_all_tasks(self):
        """Affiche toutes les taches"""
        tasks = self.controller.get_all_tasks()
        self.view.display_tasks(tasks, f"Toutes les taches ({len(tasks)})")

    def display_tasks_by_status(self):
        """Affiche les taches filtrées par statut"""
        self.view.display_status_menu()
        choice = self.view.get_input("Choisissez un statut (1-3)")

        status_map = {
            "1": TaskStatus.TODO,
            "2": TaskStatus.IN_PROGRESS,
            "3": TaskStatus.DONE
        }

        if choice not in status_map:
            self.view.display_error("Choix invalide.")
            return

        status = status_map[choice]
        tasks = self.controller.get_tasks_by_status(status)
        self.view.display_tasks(tasks, f"Taches - {status.value} ({len(tasks)})")

    def update_task(self):
        """Modifie une tache existante"""
        # Afficher d'abord toutes les taches (Option C)
        tasks = self.controller.get_all_tasks()
        self.view.display_tasks(tasks, f"Toutes les taches ({len(tasks)})")

        if not tasks:
            return

        task_id = self.view.get_input("ID de la tache a modifier")

        try:
            task_id = int(task_id)
        except ValueError:
            self.view.display_error("L'ID doit etre un nombre.")
            return

        task = self.controller.get_task_by_id(task_id)
        if not task:
            self.view.display_error(f"Aucune tache trouvée avec l'ID {task_id}.")
            return

        self.view.display_task_details(task)

        new_title = self.view.get_input("Nouveau titre (laisser vide pour conserver)")
        new_description = self.view.get_input("Nouvelle description (laisser vide pour conserver)")

        if new_title or new_description:
            self.controller.update_task(
                task_id,
                new_title if new_title else None,
                new_description if new_description else None
            )
            self.view.display_success("Tache mise aa jour avec succés!")
        else:
            self.view.display_info("Aucune modification effectuée.")

    def change_task_status(self):
        """Change le statut d'une tache"""
        # Afficher d'abord toutes les taches (Option C)
        tasks = self.controller.get_all_tasks()
        self.view.display_tasks(tasks, f"Toutes les taches ({len(tasks)})")

        if not tasks:
            return

        task_id = self.view.get_input("ID de la tache")

        try:
            task_id = int(task_id)
        except ValueError:
            self.view.display_error("L'ID doit etre un nombre.")
            return

        task = self.controller.get_task_by_id(task_id)
        if not task:
            self.view.display_error(f"Aucune tache trouvée avec l'ID {task_id}.")
            return

        self.view.display_status_menu()
        choice = self.view.get_input("Nouveau statut (1-3)")

        status_map = {
            "1": TaskStatus.TODO,
            "2": TaskStatus.IN_PROGRESS,
            "3": TaskStatus.DONE
        }

        if choice not in status_map:
            self.view.display_error("Choix invalide.")
            return

        new_status = status_map[choice]
        self.controller.update_task_status(task_id, new_status)
        self.view.display_success(f"Statut changé en: {new_status.value}")

    def delete_task(self):
        """Supprime une tache"""
        # Afficher d'abord toutes les taches (Option C)
        tasks = self.controller.get_all_tasks()
        self.view.display_tasks(tasks, f"Toutes les taches ({len(tasks)})")

        if not tasks:
            return

        task_id = self.view.get_input("ID de la tache a supprimer")

        try:
            task_id = int(task_id)
        except ValueError:
            self.view.display_error("L'ID doit etre un nombre.")
            return

        task = self.controller.get_task_by_id(task_id)
        if not task:
            self.view.display_error(f"Aucune tache trouvée avec l'ID {task_id}.")
            return

        confirmation = self.view.get_input(f"ates-vous sur de vouloir supprimer '{task.title}'? (o/n)")

        if confirmation.lower() in ['o', 'oui', 'y', 'yes']:
            self.controller.delete_task(task_id)
            self.view.display_success("Tache supprimée avec succés!")
        else:
            self.view.display_info("Suppression annulée.")

    def quit_app(self):
        """Quitte l'application"""
        total_tasks = self.controller.get_task_count()
        self.view.display_info(f"Au revoir! Vous avez {total_tasks} tache(s) enregistrée(s).")
        self.running = False


def main():
    """Fonction principale"""
    app = ToDoListApp()
    app.run()


if __name__ == "__main__":
    main()
