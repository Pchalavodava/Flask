const previewColor = document.getElementById('color');
const selectedColor = document.getElementById('favorite-color');
const clickOnMeButton = document.getElementById('press-button');
const name = document.getElementById('name');
const email = document.getElementById('email');
const emoji = document.getElementById('emoji');
const surpriseButton = document.getElementById('escape-button');
const secretButton = document.getElementById('secret-button');
const secretMessage = document.getElementById('secret-message');

selectedColor.addEventListener('input', () => {
    previewColor.style.backgroundColor = selectedColor.value;
})

clickOnMeButton.addEventListener('click', () => {
    name.value = 'Bu-bu';
    email.value = 'La-la';
    selectedColor.value = 'You will need to fill in again';
    emoji.style.display = 'inline-block'
    setTimeout(() => {emoji.style.display = 'none'}, 2000)
})

surpriseButton.addEventListener('mouseover', () => {
    const x = Math.random() * (window.innerWidth - surpriseButton.offsetWidth);
    const y = Math.random() * (window.innerHeight - surpriseButton.offsetHeight);
    surpriseButton.style.left = `${x}px`;
    surpriseButton.style.top = `${y}px`;
});

secretButton.addEventListener('click', () => {
    secretMessage.style.display = 'inline-block'
    setTimeout(() => {secretMessage.style.display = 'none'}, 2000)
})

