function increaseAdult() {
    var displayAdult = document.getElementById('displayAdult');
    var currentAdult = parseInt(displayAdult.innerHTML);
    displayAdult.innerHTML = currentAdult + 1;
    calculateTotalPrice();
}

function decreaseAdult() {
    var displayAdult = document.getElementById('displayAdult');
    var currentAdult = parseInt(displayAdult.innerHTML);
    if (currentAdult > 0) {
        displayAdult.innerHTML = currentAdult - 1;
        calculateTotalPrice();
    }
}

function increaseChild() {
    var displayChild = document.getElementById('displayChild');
    var currentChild = parseInt(displayChild.innerHTML);
    displayChild.innerHTML = currentChild + 1;
    calculateTotalPrice();
}

function decreaseChild() {
    var displayChild = document.getElementById('displayChild');
    var currentChild = parseInt(displayChild.innerHTML);
    if (currentChild > 0) {
        displayChild.innerHTML = currentChild - 1;
        calculateTotalPrice();
    }
}

function calculateTotalPrice() {
    var priceElement = document.querySelector('.prices h3');
    var price = parseFloat(priceElement.innerHTML);
    var adultCount = parseInt(document.getElementById('displayAdult').innerHTML);
    var childCount = parseInt(document.getElementById('displayChild').innerHTML);
    var totalPrice = price * adultCount + (price / 2) * childCount;
    document.querySelector('.totalPrice').innerHTML = totalPrice.toFixed(2);
}
