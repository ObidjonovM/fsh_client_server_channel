
function otmenFunction (){
    window.open('/clients/login', '_self');
} 

const login_open = document.getElementById('login_open');
login_open.addEventListener('click', function () {
    window.open('/clients/login', '_self');
})