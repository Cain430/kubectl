from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (could be a database in a real application)
tasks = [
    {"id": 1, "title": "Task 1", "completed": False},
    {"id": 2, "title": "Task 2", "completed": True}
]

# Endpoint to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

# Endpoint to get a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify({"task": task})
    return jsonify({"message": "Task not found"}), 404

# Endpoint to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        return jsonify({"message": "Invalid request"}), 400

    new_task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'completed': False
    }
    tasks.append(new_task)
    return jsonify({"task": new_task}), 201

if __name__ == '__main__':
    app.run(debug=True)
