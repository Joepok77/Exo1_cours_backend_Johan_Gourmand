import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from controllers.task_controller import TaskController
from views.cli_view import CLIView


class ToDoListApp:

    def __init__(self):
        self.controller = TaskController()
        self.view = CLIView()
        self.running = True

    def run(self):
        self.view.display_info("Bienvenue dans votre gestionnaire de taches!")

        while self.running:
            try:
                self.view.display_menu()
                choice = self.view.get_input("Choisissez une option (1-4)")

                if choice == "1":
                    self.add_task()
                elif choice == "2":
                    self.display_all_tasks()
                elif choice == "3":
                    self.delete_task()
                elif choice == "4":
                    self.quit_app()
                else:
                    self.view.display_error("Option invalide. Choisissez entre 1 et 4.")

            except KeyboardInterrupt:
                print("\n")
                self.quit_app()
            except Exception as e:
                self.view.display_error(f"Une erreur est survenue: {str(e)}")

    def add_task(self):
        title = self.view.get_input("Titre de la tache")
        if not title:
            self.view.display_error("Le titre ne peut pas etre vide.")
            return

        description = self.view.get_input("Description (optionnel)")

        task = self.controller.create_task(title, description)
        self.view.display_success(f"Tache créée avec succés! (ID: {task.id})")

    def display_all_tasks(self):
        tasks = self.controller.get_all_tasks()
        self.view.display_tasks(tasks, f"Toutes les taches ({len(tasks)})")

    def delete_task(self):
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

        confirmation = self.view.get_input(f"Etes-vous sur de vouloir supprimer '{task.title}'? (o/n)")

        if confirmation.lower() in ['o', 'oui', 'y', 'yes']:
            self.controller.delete_task(task_id)
            self.view.display_success("Tache supprimée avec succés!")
        else:
            self.view.display_info("Suppression annulée.")

    def quit_app(self):
        self.view.display_success("au revoir.")
        self.running = False


def main():
    app = ToDoListApp()
    app.run()


if __name__ == "__main__":
    main()
