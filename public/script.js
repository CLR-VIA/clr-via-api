function toggleMode() {
    const body = document.body;
    const content = document.querySelector('.content');
    const modeToggle = document.getElementById('modeToggle');
    if (modeToggle.checked) {
        body.classList.replace('light-mode', 'dark-mode');
        content.classList.replace('light-mode', 'dark-mode');
    } else {
        body.classList.replace('dark-mode', 'light-mode');
        content.classList.replace('dark-mode', 'light-mode');
    }
}
