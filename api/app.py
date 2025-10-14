"""
API REST Flask pour le gestionnaire de taches ToDoList
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
from pathlib import Path

# Ajouter le dossier api au path
sys.path.insert(0, str(Path(__file__).parent))

from controllers.task_controller import TaskController
from models.task import TaskStatus

# Initialiser Flask
app = Flask(__name__)
CORS(app)  # Permet les requêtes depuis n'importe quelle origine (frontend)

# Initialiser le controller
controller = TaskController()


# Routes de l'API

@app.route('/api/health', methods=['GET'])
def health_check():
    """Vérifier que l'API fonctionne"""
    return jsonify({
        'status': 'ok',
        'message': 'ToDoList API is running'
    }), 200


@app.route('/api/tasks', methods=['GET'])
def get_all_tasks():
    """Récupérer toutes les taches"""
    tasks = controller.get_all_tasks()
    return jsonify({
        'success': True,
        'count': len(tasks),
        'tasks': [task.to_dict() for task in tasks]
    }), 200


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Récupérer une tache par son ID"""
    task = controller.get_task_by_id(task_id)

    if not task:
        return jsonify({
            'success': False,
            'error': f'Task with ID {task_id} not found'
        }), 404

    return jsonify({
        'success': True,
        'task': task.to_dict()
    }), 200


@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Créer une nouvelle tache"""
    data = request.get_json()

    if not data or 'title' not in data:
        return jsonify({
            'success': False,
            'error': 'Title is required'
        }), 400

    title = data['title']
    description = data.get('description', '')

    task = controller.create_task(title, description)

    return jsonify({
        'success': True,
        'message': 'Task created successfully',
        'task': task.to_dict()
    }), 201


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Modifier une tache existante"""
    task = controller.get_task_by_id(task_id)

    if not task:
        return jsonify({
            'success': False,
            'error': f'Task with ID {task_id} not found'
        }), 404

    data = request.get_json()

    title = data.get('title')
    description = data.get('description')

    controller.update_task(task_id, title, description)

    updated_task = controller.get_task_by_id(task_id)

    return jsonify({
        'success': True,
        'message': 'Task updated successfully',
        'task': updated_task.to_dict()
    }), 200


@app.route('/api/tasks/<int:task_id>/status', methods=['PATCH'])
def update_task_status(task_id):
    """Changer le statut d'une tache"""
    task = controller.get_task_by_id(task_id)

    if not task:
        return jsonify({
            'success': False,
            'error': f'Task with ID {task_id} not found'
        }), 404

    data = request.get_json()

    if not data or 'status' not in data:
        return jsonify({
            'success': False,
            'error': 'Status is required'
        }), 400

    status_str = data['status'].upper()

    try:
        new_status = TaskStatus[status_str]
    except KeyError:
        return jsonify({
            'success': False,
            'error': f'Invalid status. Must be one of: TODO, IN_PROGRESS, DONE'
        }), 400

    controller.update_task_status(task_id, new_status)

    updated_task = controller.get_task_by_id(task_id)

    return jsonify({
        'success': True,
        'message': f'Task status updated to {new_status.value}',
        'task': updated_task.to_dict()
    }), 200


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Supprimer une tache"""
    task = controller.get_task_by_id(task_id)

    if not task:
        return jsonify({
            'success': False,
            'error': f'Task with ID {task_id} not found'
        }), 404

    controller.delete_task(task_id)

    return jsonify({
        'success': True,
        'message': 'Task deleted successfully'
    }), 200


@app.route('/api/tasks/status/<status>', methods=['GET'])
def get_tasks_by_status(status):
    """Récupérer les taches par statut"""
    status_str = status.upper()

    try:
        task_status = TaskStatus[status_str]
    except KeyError:
        return jsonify({
            'success': False,
            'error': f'Invalid status. Must be one of: TODO, IN_PROGRESS, DONE'
        }), 400

    tasks = controller.get_tasks_by_status(task_status)

    return jsonify({
        'success': True,
        'status': task_status.value,
        'count': len(tasks),
        'tasks': [task.to_dict() for task in tasks]
    }), 200


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Obtenir des statistiques sur les taches"""
    all_tasks = controller.get_all_tasks()

    stats = {
        'total': len(all_tasks),
        'todo': len([t for t in all_tasks if t.status == TaskStatus.TODO]),
        'in_progress': len([t for t in all_tasks if t.status == TaskStatus.IN_PROGRESS]),
        'done': len([t for t in all_tasks if t.status == TaskStatus.DONE])
    }

    return jsonify({
        'success': True,
        'stats': stats
    }), 200


# Gestionnaire d'erreurs
@app.errorhandler(404)
def not_found(error):
    """Gérer les routes non trouvées"""
    return jsonify({
        'success': False,
        'error': 'Route not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Gérer les erreurs internes du serveur"""
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500


if __name__ == '__main__':
    # Lancer le serveur Flask
    print("🚀 ToDoList API is starting...")
    print("📍 API disponible sur: http://localhost:5000")
    print("📖 Health check: http://localhost:5000/api/health")
    app.run(debug=True, host='0.0.0.0', port=5000)
