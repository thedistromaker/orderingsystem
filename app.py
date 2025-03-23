from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

order_queue = []
current_order = []

PRICES = {
    "Cappuccino": 3.50,
    "Espresso": 2.50,
    "Latte": 4.00,
    "Milk": 0.50,
    "Extra Shot": 1.00
}

@app.route('/')
def index():
    return "Redirecting...", 302, {'Location': '/register'}

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/kds')
def kds():
    return render_template('kds.html')

@socketio.on('addOrder')
def add_order(item):
    current_order.append(item)
    socketio.emit('updateOrder', {'items': current_order, 'total': sum(PRICES[i] for i in current_order)})

@socketio.on('submitOrder')
def submit_order():
    if current_order:
        order_queue.append(list(current_order))
        current_order.clear()
        socketio.emit('updateQueue', order_queue)
        socketio.emit('updateOrder', {'items': [], 'total': 0})

@socketio.on('finishOrder')
def finish_order():
    if order_queue:
        order_queue.pop(0)
        socketio.emit('updateQueue', order_queue)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
