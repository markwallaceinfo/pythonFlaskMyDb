import os
import signal
import db_connector
# web_app.py

from flask import Flask, render_template

# from Project import db_connector

app = Flask(__name__)


@app.route('/users/get_user_data/<int:user_id>', methods=['GET'])
def get_user_data(user_id):
    try:
        user_name = db_connector.add_user(user_id)
        if user_name:
            return render_template('user_data.html', user_name=user_name)
        else:
            return render_template('error.html', error="User ID not found")

    except Exception as e:
        return render_template('error.html', error=str(e))


def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stop'


app.run(host='127.0.0.1', debug=True, port=5001)
