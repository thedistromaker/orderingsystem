var socket = io();

socket.on('updateOrder', function(data) {
    document.getElementById('totalAmount').textContent = data.total.toFixed(2);

    let orderList = document.getElementById('orderList');
    orderList.innerHTML = '';
    data.items.forEach(item => {
        let li = document.createElement('li');
        li.textContent = item;
        orderList.appendChild(li);
    });
});

document.querySelectorAll('.order-btn').forEach(button => {
    button.addEventListener('click', function() {
        let item = this.getAttribute('data-item');
        socket.emit('addOrder', item);
    });
});

document.getElementById('submitOrder').addEventListener('click', function() {
    socket.emit('submitOrder');
});

document.getElementById('finishOrder').addEventListener('click', function() {
    socket.emit('finishOrder');
});
