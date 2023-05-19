const navbarToggle = document.querySelector('.navbar__toggle');

navbarToggle.addEventListener('click', () => {
  navbarToggle.classList.toggle('active');
  document.querySelector('.navbar__items').classList.toggle('active');
});


window.addEventListener('resize', () => {
  if (window.innerWidth > 768) {
    document.querySelector('.navbar__items').classList.remove('active');
    navbarToggle.classList.remove('active');
  }
});

// image upload section is here 

const uploadButton = document.getElementById("upload-button");
const fileInput = document.getElementById("image-upload");

uploadButton.addEventListener("click", () => {
  const file = fileInput.files[0];
  if (file) {
    // Perform validation and upload
    console.log("Uploading file:", file);
  } else {
    alert("Please select an image file to upload.");
  }
});

// experimental section is here 



////////////////////////////////////////////////////////

$(document).ready(function() {
    // Add smooth scrolling to features section
    $('a[href="#features"]').on('click', function(event) {
      if (this.hash !== '') {
        event.preventDefault();
  
        var hash = this.hash;
  
        $('html, body').animate({
          scrollTop: $(hash).offset().top
        }, 800, function(){
     
          window.location.hash = hash;
        });
      }
    });
  });

  
  // call to action section functanality

  const ctaButton = document.querySelector('.cta-button');

ctaButton.addEventListener('click', () => {
  // Add code here for button functionality
});

/* close menu function to click outside that */

const closeMenu = () => {
  const menu = document.querySelector('.menu');
  menu.classList.remove('active');
};

document.addEventListener('click', function(event) {
  const menu = document.querySelector('.menu');
  const toggle = document.querySelector('.menu-toggle');
  const target = event.target;
  const isClickInsideMenu = menu.contains(target);
  const isClickInsideToggle = toggle.contains(target);

  if (!isClickInsideMenu && !isClickInsideToggle && menu.classList.contains('active')) {
    closeMenu();
  }
});
