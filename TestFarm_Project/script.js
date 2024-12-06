// Simple Carousel Implementation
let currentIndex = 0;
const images = document.querySelectorAll('.carousel img');

function showNextImage() {
    images[currentIndex].style.display = 'none'; // Hide current image
    currentIndex = (currentIndex + 1) % images.length; // Go to next image
    images[currentIndex].style.display = 'block'; // Show next image
}

// Initially show the first image
if (images.length > 0) {
    images[currentIndex].style.display = 'block';
}

// Change image every 3 seconds
if (images.length > 0) {
    setInterval(showNextImage, 3000);
}
