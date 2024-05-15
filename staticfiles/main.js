// Button Scroll Up 
let scrollUpButton = document.querySelector(".scrollUp");

scrollUpButton.onclick = function () {
    window.scrollTo({
        top: 0,
        behavior: "smooth",
    });
};

window.onscroll = function () {
    if (window.scrollY >= 800) {
        scrollUpButton.style.display = "block";
    } else {
        scrollUpButton.style.display = "none";
    }
};


// ******************************* //
// Login & Register Form

let loginForm = document.querySelector(".login-form");
let registerForm = document.querySelector(".register-form");

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
/********   Request Form   ********/
let requestForm = document.querySelector(".request");
function showFormRequest() {
    requestForm.classList.add("reqActive");
}
function hideRequest() {
    requestForm.classList.remove("reqActive");
}


