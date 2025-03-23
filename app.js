const socket = io();

function addOrder(item) {
    let orderSummary = document.getElementById('order-summary');
    orderSummary.innerHTML += `<p>${item}</p>`;
}

function submitOrder() {
    let orders = document.getElementById('order-summary').innerHTML;
    socket.emit('add_order', orders);
}

socket.on('update_orders', function (orders) {
    document.getElementById('orders').innerHTML = orders.join("<br>");
});

function finishOrder() {
    socket.emit('finish_order');
}
