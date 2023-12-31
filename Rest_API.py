import os
import signal

from flask import Flask, request
from flask import request, json, jsonify
from db_connector import add_user

app = Flask(__name__)


# supported methods
@app.route('/data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        try:
            user_name = request.json.get('user_name')
            user_name = request_data.get('user_name')
            add_user(user_id, user_name)
            return jsonify({'status', 'ok', 'user_added' < user_name > 200})
        except:
            return jsonify({"status", "error", "reason", "id already exists" < user_name > 500})


    elif request.method == 'GET':
        request_data = request.json
        try:
            user_name = request_data.get('user_name')
            # add_user(user_id, user_name)
            return jsonify({'status', 'ok', 'user_name' < user_name > 200})
        except:
            return jsonify()

    elif request.method == 'PUT':
        request_data = request.json
        try:
            user_name = request_data.get('user_name')
            add_user(user_id, user_name)
            user_name = request_data.get(user_id)
            return jsonify({'status', 'ok', 'user_updated' < user_name > 200})
        except:
            return jsonify({'status', 'error', 'reason', 'no such id', 500})

    elif request.method == 'DELETE':
        user = request.get_data(user_id)
        if user == None:
            return jsonify({"status": "ok", "user_deleted": user_id}), 200
        else:
            return jsonify({"status": "error", "reason": "no such id"}), 500


def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stop'


app.run(host='127.0.0.1', debug=True, port=5000)
