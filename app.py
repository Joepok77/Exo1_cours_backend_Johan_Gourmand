from flask import Flask, request, jsonify
from controllers.task_controller import TaskController

# Controller Flask
controller = TaskController()

# Configuration Flask
app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def get_all_tasks():
    tasks = controller.get_all_tasks()
    return jsonify({
        'success': True,
        'count': len(tasks),
        'tasks': [task.to_dict() for task in tasks]
    }), 200


@app.route('/tasks', methods=['POST'])
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


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    success = controller.delete_task(task_id)
    if not success:
        return jsonify({'success': False, 'error': 'Task not found'}), 404
    return jsonify({'success': True, 'message': 'Task deleted'}), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
