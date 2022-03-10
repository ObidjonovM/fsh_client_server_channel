window.addEventListener('load', function () {
    let input = document.getElementById('clientname');
    input.focus();
})


function logoutClient() {
    window.open('/clients/logout', '_self');
}


const register_open = document.getElementById('register_open');


register_open.addEventListener('click', () => {
    window.open('/clients/register', '_self');
})

const change_password = document.getElementById('change_password');
change_password.addEventListener('click', function () {
    window.open('/clients/change_password', '_self');
})


//alohida
const loginBtn = document.querySelector('.auth .login');
const signupBtn = document.querySelector('.auth .signup');

const loginSection = document.querySelector('#login');
const signupSection = document.querySelector('#signup');

signupBtn.addEventListener('click', function () {
    loginSection.classList.remove('show');
    signupSection.classList.add('show');
    loginBtn.classList.remove('selected');
    signupBtn.classList.add('selected');
});

loginBtn.addEventListener('click', function () {
    signupSection.classList.remove('show');
    loginSection.classList.add('show');
    signupBtn.classList.remove('selected');
    loginBtn.classList.add('selected');
});
//alohida
