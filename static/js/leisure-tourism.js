
document.addEventListener("DOMContentLoaded", function() {
    var slideIndex = 1;
    showSlides(slideIndex);

    function plusSlides(n) {
        showSlides(slideIndex += n);
    }

    function currentSlide(n) {
        showSlides(slideIndex = n);
    }

    function showSlides(n) {
        var i;
        var slides = document.getElementsByClassName("mySlides");
        var dots = document.getElementsByClassName("dot");
        if (n > slides.length) { slideIndex = 1 }
        if (n < 1) { slideIndex = slides.length }
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
        }
        slides[slideIndex - 1].style.display = "block";
        dots[slideIndex - 1].className += " active";
    }

    // Attach click handlers for next/prev buttons
    document.querySelector(".prev").addEventListener("click", function() {
        plusSlides(-1);
    });
    document.querySelector(".next").addEventListener("click", function() {
        plusSlides(1);
    });

    // Attach click handlers for dots
    var dots = document.getElementsByClassName("dot");
    for (i = 0; i < dots.length; i++) {
        (function(index) {
            dots[index].addEventListener("click", function() {
                currentSlide(index + 1);
            });
        })(i);
    }
});
