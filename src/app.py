from flask import Flask, request, Response, render_template, jsonify
from flask_cors import CORS
from src.models import todo

app = Flask(__name__)
CORS(app)

todo = todo.Todo()

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html'), 200

# todo routes
@app.route('/todos/', methods=['GET'])
def get_tasks():
    return jsonify(todo.find({})), 200


@app.route('/todos/<string:todo_id>/', methods=['GET'])
def get_task(todo_id):
    return todo.find_by_id(todo_id), 200


@app.route('/todos/', methods=['POST'])
def add_tasks():
    if request.method == "POST":
        title = request.form['title']
        body = request.form['body']
        response = todo.create({'title': title, 'body': body})
        return response, 201


@app.route('/todos/<string:todo_id>/', methods=['PUT'])
def update_tasks(todo_id):
    if request.method == "PUT":
        title = request.form['title']
        body = request.form['body']
        response = todo.update(todo_id, {'title': title, 'body': body})
        return response, 201


@app.route('/todos/<string:todo_id>/', methods=['DELETE'])
def delete_tasks(todo_id):
    if request.method == "DELETE":
        todo.delete(todo_id)
        return "Record Deleted"

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()