function checkAndApplyTheme() {
    const isLightMode = localStorage.getItem("lightMode") === "true";
    document.body.classList.toggle("lightmode", isLightMode);
    
    const themeIcon = document.getElementById('themeIconInner');
    themeIcon.classList.toggle('fa-sun', isLightMode);
    themeIcon.classList.toggle('fa-moon', !isLightMode);
}

window.onload = checkAndApplyTheme();

function toggleTheme() {
    const body = document.body;
    body.classList.toggle('lightmode');

    const isLightMode = body.classList.contains('lightmode');
    localStorage.setItem("lightMode", isLightMode);
    
    const themeIcon = document.getElementById('themeIconInner');
    themeIcon.classList.toggle('fa-sun', isLightMode);
    themeIcon.classList.toggle('fa-moon', !isLightMode);
}

// helpers.js

const hamburger = document.querySelector('.hamburger');
const nav = document.querySelector('.nav');

hamburger.addEventListener("click", () => {
    nav.classList.toggle("active");
});

const reflexButton = document.querySelector('#dialog_button')
const modal = document.querySelector('#dialog')
const modalClose = document.querySelector('#close')

reflexButton.onclick = function () {
    modal.show();
}

modalClose.onclick = function () {
    modal.close();
}
