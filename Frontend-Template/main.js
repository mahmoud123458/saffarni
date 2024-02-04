
// let searchBtn = document.querySelector("#search-btn");
// let searchForm = document.querySelector(".search-form");
let loginForm = document.querySelector(".login-form");
let registerForm = document.querySelector(".register-form");
// function showBar(){
//     searchBtn.classList.toggle("fa-times")
//     searchForm.classList.toggle("active")
// }

function showForm() {
    loginForm.classList.add("active");
}

function showFormRegister() {
    registerForm.classList.add("active");
    loginForm.classList.remove("active");
}

function hideForm() {
    loginForm.classList.remove("active");
    registerForm.classList.remove("active");
}

let requestForm = document.querySelector(".request");
function showFormRequest() {
    requestForm.classList.add("reqActive");
}
function hideRequest() {
    requestForm.classList.remove("reqActive");
}
