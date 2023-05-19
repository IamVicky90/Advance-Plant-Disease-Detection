// Add animation to the button when clicked
const introBtn = document.querySelector('.intro-btn');

introBtn.addEventListener('click', () => {
  introBtn.classList.add('btn-clicked');
});

introBtn.addEventListener('animationend', () => {
  introBtn.classList.remove('btn-clicked');
});
