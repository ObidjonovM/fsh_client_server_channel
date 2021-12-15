// document.getElementById('error_username').style.display = "none";

function validateForm() {


    var username = document.getElementById('username').value;

    var password = document.getElementById('password').value;

    var new_password = document.getElementById('new_password').value;

    var new_confirm_password = document.getElementById('new_confirm_password').value;

    if (username == "") {

        document.getElementById('error_username').innerHTML = "**Введите имя!";
        document.getElementById('error_username').style.display = "block";

        return false;
    }


    if (!isNaN(username)) {
        document.getElementById('error_username').innerHTML = "**Только . и письмо должно быть обработано!";
        document.getElementById('error_username').style.display = "block";


        return false;
    }

    if (password == "") {

        document.getElementById('error_password').innerHTML = "**Введите пароль, пожалуйста!";
        document.getElementById('error_password').style.display = "block";


        return false;
    }


    if (new_password == "") {

        document.getElementById('error_new_password').innerHTML = "**Пожалуйста, введите новый пароль!";
        document.getElementById('error_new_password').style.display = "block";


        return false;
    }


    if (new_confirm_password == "") {

        document.getElementById('error_new_confirm_password').innerHTML = "**Пожалуйста, введите новый пароль для подтверждения!"
        document.getElementById('error_new_confirm_password').style.display = "block";
        return false;
    }


    if (new_password != new_confirm_password) {

        var myForm = document.getElementById('myForm');
        myForm.addEventListener('submit', function (event) {
            event.preventDefault();

        });
        alert("Пароль не тот!");
        return false;

    }


};



const back = document.getElementById('back');
back.addEventListener('click', function () {
    window.open('/clients/login', '_self');
})

