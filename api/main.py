import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from flask import Flask, request, jsonify

from controllers.task_controller import TaskController
from views.cli_view import CLIView
from models.task import TaskStatus

# Controller partagé entre CLI et Flask
controller = TaskController()

# Configuration Flask
app = Flask(__name__)



# Routes Flask API
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'message': 'API is running'}), 200


@app.route('/api/tasks', methods=['GET'])
def get_all_tasks():
    tasks = controller.get_all_tasks()
    return jsonify({
        'success': True,
        'count': len(tasks),
        'tasks': [task.to_dict() for task in tasks]
    }), 200


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = controller.get_task_by_id(task_id)
    if not task:
        return jsonify({'success': False, 'error': 'Task not found'}), 404
    return jsonify({'success': True, 'task': task.to_dict()}), 200


@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'success': False, 'error': 'Title is required'}), 400

    task = controller.create_task(data['title'], data.get('description', ''))
    return jsonify({
        'success': True,
        'message': 'Task created',
        'task': task.to_dict()
    }), 201


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = controller.get_task_by_id(task_id)
    if not task:
        return jsonify({'success': False, 'error': 'Task not found'}), 404

    controller.delete_task(task_id)
    return jsonify({'success': True, 'message': 'Task deleted'}), 200


@app.route('/api/tasks/<int:task_id>/status', methods=['PATCH'])
def update_task_status(task_id):
    task = controller.get_task_by_id(task_id)
    if not task:
        return jsonify({'success': False, 'error': 'Task not found'}), 404

    data = request.get_json()
    if not data or 'status' not in data:
        return jsonify({'success': False, 'error': 'Status is required'}), 400

    try:
        new_status = TaskStatus[data['status'].upper()]
    except KeyError:
        return jsonify({'success': False, 'error': 'Invalid status'}), 400

    controller.update_task_status(task_id, new_status)
    updated_task = controller.get_task_by_id(task_id)
    return jsonify({
        'success': True,
        'message': 'Status updated',
        'task': updated_task.to_dict()
    }), 200


# Mode CLI
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
        total_tasks = self.controller.get_task_count()
        self.view.display_info(f"Au revoir! Vous avez {total_tasks} tache(s) enregistrée(s).")
        self.running = False


def main():
    print("\n=== TODOLIST - MODE DE DEMARRAGE ===")
    print("1. Mode CLI (Terminal)")
    print("2. Mode API Flask (Serveur web)")
    print("=====================================")

    choice = input("\nChoisissez un mode (1 ou 2): ").strip()

    if choice == "1":
        app_cli = ToDoListApp()
        app_cli.run()
    elif choice == "2":
        print("\n🚀 Lancement du serveur Flask...")
        print("📍 API disponible sur: http://localhost:5000")
        print("📖 Endpoints:")
        print("   - GET  /api/health")
        print("   - GET  /api/tasks")
        print("   - POST /api/tasks")
        print("   - GET  /api/tasks/<id>")
        print("   - DELETE /api/tasks/<id>")
        print("   - PATCH /api/tasks/<id>/status")
        print("\nAppuyez sur Ctrl+C pour arrêter\n")
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("Choix invalide. Utilisez 1 ou 2.")


if __name__ == "__main__":
    main()
