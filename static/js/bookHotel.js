/********   Details Page   *********/

let thePrice = 3000;
let price = 0;

let numRoom = document.getElementById("displayNumRoom");
let numAdult = document.getElementById("displayAdults");
let numChild = document.getElementById("displayChildren");
let totalP = document.querySelector(".totalPrice");

let numOfRoom = 1;
function increaseNumRoom() {
    if (numOfRoom < 4) {
        numOfRoom++;
        numRoom.innerHTML = numOfRoom;
        price = `${parseInt(numOfRoom)* thePrice}`;
        totalP.innerHTML = `${parseInt(price)} EG`;
    }
}
function decreaseNumRoom() {
    if (numOfRoom > 1) {
        numOfRoom--;
        numRoom.innerHTML = numOfRoom;
        price = `${parseInt(numOfRoom) * thePrice}`;
        totalP.innerHTML = `${parseInt(price)} EG`;
    }
}
let valAdult = 1;
function increaseAdult() {
    if (valAdult < 6) {
        valAdult++;
        numAdult.innerHTML = valAdult;
        price = `${thePrice + valAdult * 1000}`;
        totalP.innerHTML = `${parseInt(price)} EG`;
    }
}
function decreaseAdult() {
    if (valAdult > 1) {
        valAdult--;
        numAdult.innerHTML = valAdult;
        price = `${thePrice + valAdult * 1000}`;
        totalP.innerHTML = `${parseInt(price)} EG`;
    }
}

let valChild = 0;
function increaseChild() {
    if (valChild < 6) {
        valChild++;
        numChild.innerHTML = valChild;
        price = `${thePrice + valChild * 600}`;
        totalP.innerHTML = `${parseInt(price)} EG`;
    }
}
function decreaseChild() {
    if (valChild > 0) {
        valChild--;
        numChild.innerHTML = valChild;
        price = `${thePrice + valChild * 600}`;
        totalP.innerHTML = `${parseInt(price)} EG`;
    }
}
price.innerHTML = thePrice;
console.log(parseInt(numAdult.textContent));
console.log(parseInt(valChild));
console.log(parseInt(price.textContent));



