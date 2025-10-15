from controllers.task_controller import TaskController
from views.cli_view import CLIView

# Controller CLI
controller = TaskController()
class ToDoListApp:

    def __init__(self):
        self.controller = controller
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

        confirmation = self.view.get_input(f"Etes-vous sur de vouloir supprimer la tache {task_id}? (o/n)")

        if confirmation.lower() in ['o', 'oui', 'y', 'yes']:
            success = self.controller.delete_task(task_id)
            if success:
                self.view.display_success("Tache supprimée avec succés!")
            else:
                self.view.display_error(f"Aucune tache trouvée avec l'ID {task_id}.")
        else:
            self.view.display_info("Suppression annulée.")

    def quit_app(self):
        total_tasks = self.controller.get_task_count()
        self.view.display_info(f"Au revoir! Vous avez {total_tasks} tache(s) enregistrée(s).")
        self.running = False


if __name__ == "__main__":
    app = ToDoListApp()
    app.run()
