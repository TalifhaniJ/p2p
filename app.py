from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def connect():
    print('Client connected')

@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(message):
    print(f'Received message: {message}')
    socketio.emit('message', message)  # Broadcast

if __name__ == '__main__':
    socketio.run(app,allow_unsafe_werkzeug=True,debug=True, host='0.0.0.0', port=1000)
