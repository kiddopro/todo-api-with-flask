from flask import Flask, request, jsonify, json
app = Flask(__name__)


todos = [
    {"label" : "My first task", "done":False},
    {"label" : "My first task2", "done":False}
]

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(request_body)
    todos_text = jsonify(todos)
    print("Incoming request with the following body", request_body)
    return todos_text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)