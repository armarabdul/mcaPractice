// Toggle Navigation Menu on Mobile Devices
document.addEventListener('DOMContentLoaded', function() {
    var menuToggle = document.querySelector('.menu-toggle');
    var menu = document.querySelector('nav ul');

    menuToggle.addEventListener('click', function() {
        menu.classList.toggle('active');
    });
});

// Image Slider Functionality
document.addEventListener('DOMContentLoaded', function() {
    var slides = document.querySelectorAll('.slide');
    var currentIndex = 0;

    function showSlide(index) {
        slides.forEach(function(slide, i) {
            slide.style.display = (i === index) ? 'block' : 'none';
        });
    }

    document.querySelector('.prev').addEventListener('click', function() {
        currentIndex = (currentIndex > 0) ? currentIndex - 1 : slides.length - 1;
        showSlide(currentIndex);
    });

    document.querySelector('.next').addEventListener('click', function() {
        currentIndex = (currentIndex < slides.length - 1) ? currentIndex + 1 : 0;
        showSlide(currentIndex);
    });

    showSlide(currentIndex); // Show the first slide initially
});

// Contact Form Validation
document.addEventListener('DOMContentLoaded', function() {
    var contactForm = document.getElementById('contactForm');
    var errorMessage = document.getElementById('error-message');

    contactForm.addEventListener('submit', function(event) {
        var name = document.getElementById('name').value.trim();
        var email = document.getElementById('email').value.trim();
        var message = document.getElementById('message').value.trim();

        if (!name || !email || !message) {
            event.preventDefault();
            errorMessage.textContent = 'Please fill in all fields.';
        } else {
            errorMessage.textContent = '';
        }
    });
});
