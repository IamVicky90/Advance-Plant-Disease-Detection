const form = document.getElementById("contact");
const nameInput = document.querySelector('input[type="text"]');
const emailInput = document.querySelector('input[type="email"]');
const phoneInput = document.querySelector('input[type="tel"]');
const messageInput = document.querySelector('textarea');

form.addEventListener("submit", function(event) {
  event.preventDefault();

  if (validateForm()) {
    const formData = new FormData(form);
    const xhr = new XMLHttpRequest();
    xhr.open("POST", form.action);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        alert("Thank you! We'll be in touch shortly.");
        form.reset();
      }
    };
    xhr.send(new URLSearchParams(formData).toString());
  }
});

function validateForm() {
  let isValid = true;
  if (nameInput.value === "") {
    nameInput.classList.add("invalid");
    isValid = false;
  } else {
    nameInput.classList.remove("invalid");
  }
  if (emailInput.value === "") {
    emailInput.classList.add("invalid");
    isValid = false;
  } else {
    emailInput.classList.remove("invalid");
  }
  if (messageInput.value === "") {
    messageInput.classList.add("invalid");
    isValid = false;
  } else {
    messageInput.classList.remove("invalid");
  }
  return isValid;
}
//  location section is here  
function initMap() {
  var myLocation = {lat: 33.651592, lng: 73.156456}; // Change these coordinates to your own location
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 14,
    center: myLocation
  });
  var marker = new google.maps.Marker({
    position: myLocation,
    map: map,
    title: 'My Location' // Change this to your own location name
  });
}

// faqs section is here 
