from flask import Flask, render_template, redirect
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

orders = []

@app.route('/')
def home():
    return redirect('/register')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/kds')
def kds():
    return render_template('kds.html')

@socketio.on('add_order')
def add_order(data):
    orders.append(data)
    socketio.emit('update_orders', orders)

@socketio.on('finish_order')
def finish_order():
    if orders:
        orders.pop(0)
        socketio.emit('update_orders', orders)

if __name__ == '__main__':
    socketio.run(app, debug=True)
