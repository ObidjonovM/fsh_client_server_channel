
function otmenFunction (){
    window.open('/clients/login', '_self');
} 

const login_open = document.getElementById('login_open');
login_open.addEventListener('click', function () {
    window.open('/clients/login', '_self');
})


const xhttp = new XMLHttpRequest();
function loginChange() {
    let clientname = document.getElementById('clientname').value;
    console.log(clientname)
    xhttp.open('Post', '/clients/user_exists', true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send(JSON.stringify({'name' : clientname}));
    let login_error = document.getElementById('login_error');
    let submit = document.getElementById('submit');

    xhttp.onreadystatechange = function (ev) {
        if (xhttp.readyState ==4 && xhttp.status == 200){
            const resp = JSON.parse(xhttp.responseText);
            if (resp['user_exists'] == true){
                let result = `<small style="color: red; font-size: 10px;">Bunday username mavjud!</small>`;
                login_error.innerHTML = result;
                submit.style.pointerEvents = 'none';
                // password.setAttribute('readonly', '');
                // confirm_password.setAttribute('readonly', '');
            }else {
                login_error.innerHTML = " ";
                submit.style.pointerEvents = 'visible';
                // password.removeAttribute('readonly');
                // confirm_password.removeAttribute('readonly');
            }
        }
    }

}







function validateForm() {


    var clientname = document.getElementById('clientname').value;

    var password = document.getElementById('password').value;

    // var new_password = document.getElementById('new_password').value;

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

        var myForm = document.getElementById('myForm');
        myForm.addEventListener('submit', function (event) {
            // event.preventDefault();
            console.log("2")
        });
        alert("Parol bir xil emas!");
        return false;
    }

};