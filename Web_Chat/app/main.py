from flask import Flask, redirect, render_template, request
from flask_socketio import SocketIO, send

from config import secret_key


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key
    return app


app = create_app()

socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')
def handle_message(message):
    print("Received message: ", message)
    if message != "User connected":
        send(message, broadcast=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    socketio.run(app, host='192.168.31.115')
