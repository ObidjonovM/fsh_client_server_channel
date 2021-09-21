document.getElementById('error_username').style.display = "none";

function validateForm() {


    var username = document.getElementById('username').value;

    var password = document.getElementById('password').value;

    var new_password = document.getElementById('new_password').value;

    var new_confirm_password = document.getElementById('new_confirm_password').value;

    if (username == "") {

        document.getElementById('error_username').innerHTML = "**Fill the first name!";
        document.getElementById('error_username').style.display = "block";

        return false;
    }


    if (!isNaN(username)) {
        document.getElementById('error_username').innerHTML = "**Faqat . va harf qatnashish kerak!";
        document.getElementById('error_username').style.display = "block";


        return false;
    }

    if (password == "") {

        document.getElementById('error_password').innerHTML = "**Fill the password please!";
        document.getElementById('error_password').style.display = "block";


        return false;
    }


    if (new_password == "") {

        document.getElementById('error_new_password').innerHTML = "**Fill the new password please!";
        document.getElementById('error_new_password').style.display = "block";


        return false;
    }


    if (new_confirm_password == "") {

        document.getElementById('error_new_confirm_password').innerHTML = "**Fill the new confirm password please!"
        document.getElementById('error_new_confirm_password').style.display = "block";
        return false;
    }


    if (new_password != new_confirm_password) {

        var myForm = document.getElementById('myForm');
        myForm.addEventListener('submit', function (event) {
            event.preventDefault();

        });
        alert("Parol bir xil emas!");
        return false;

    } else {
        alert("Tabriklaymiz parol o'zgardi!")
    }


};



const back = document.getElementById('back');
back.addEventListener('click', function () {
    window.open('/clients/login', '_self');
})

