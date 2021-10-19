from flask import Flask, request, jsonify
import json
app = Flask(__name__)


todos = [
    {"done": True,"label":"Sample Todo 2"}
]

@app.route('/todos', methods=['POST', 'GET'])
def add_new_todo():
    if request.method == 'GET':
        return jsonify(todos)
    else:
        request_body = request.data
        decoded_object = json.loads(request_body)
        todos.append(decoded_object)
        return jsonify(todos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)