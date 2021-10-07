function otmenFunction() {
    window.open('/clients/login', '_self');
}

const login_open = document.getElementById('login_open');
login_open.addEventListener('click', function () {
    window.open('/clients/login', '_self');
})


const xhttp = new XMLHttpRequest();

function loginChange() {
    let clientname = document.getElementById('clientname').value;
    let login_error = document.getElementById('login_error');
    let submit = document.getElementById('submit');
    console.log(clientname)
    xhttp.open('Post', '/clients/user_exists', true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send(JSON.stringify({'name': clientname}));


    xhttp.onreadystatechange = function (ev) {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            const resp = JSON.parse(xhttp.responseText);
            if (resp['user_exists'] == true) {
                let result = `<small style="color: red; font-size: 10px;">Bunday username mavjud!</small>`;
                login_error.innerHTML = result;
                submit.style.pointerEvents = 'none';
            } else {
                login_error.innerHTML = " ";
                submit.style.pointerEvents = 'visible';
            }
        }
    }

}


function validateForm() {


    var clientname = document.getElementById('clientname').value;

    var password = document.getElementById('password').value;

    var confirm_password = document.getElementById('confirm_password').value;

    if (clientname == "") {

        document.getElementById('login_error').innerHTML = "**Fill the first name!";
        document.getElementById('login_error').style.display = "block";

        return false;
    }

    if (!isNaN(clientname)) {
        document.getElementById('login_error').innerHTML = "**Faqat . va harf qatnashish kerak!";
        document.getElementById('login_error').style.display = "block";


        return false;
    }

    if (password == "") {

        document.getElementById('error_password').innerHTML = "**Fill the password please!";
        document.getElementById('error_password').style.display = "block";


        return false;
    }

    if (confirm_password == "") {

        document.getElementById('confirm_error_password').innerHTML = "**Fill the new password please!";
        document.getElementById('confirm_error_password').style.display = "block";


        return false;
    }

    if (password != confirm_password) {

        const modal = document.querySelector('.modal');
        const overlay = document.querySelector('.overlay');
        modal.classList.remove('hidden');
        overlay.classList.remove('hidden');

        return false;
    } else {
        alert("Вы зарегистрированы!")
    }

}

const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.close-modal');

const closeModal = function () {
    modal.classList.add('hidden');
    overlay.classList.add('hidden');
};

btnCloseModal.addEventListener('click', closeModal);