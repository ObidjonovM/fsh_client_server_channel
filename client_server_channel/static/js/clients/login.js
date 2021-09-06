function logoutClient() {
    window.open('/clients/logout', '_self');
}

document.getElementById('error-small').style.display = "none";


const register_open = document.getElementById('register-open');

register_open.addEventListener('click', () => {
    window.open('/clients/register', '_self');
})