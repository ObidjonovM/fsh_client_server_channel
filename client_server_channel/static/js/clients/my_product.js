// modal open
'use strict';
//Измените описание!
const overlay1 = document.querySelector('.overlay1');
const modal1 = document.querySelector('.modal1');
//Измените описание!

// const modal2 = document.querySelector('.modal2');

const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
// const overlay2 = document.querySelector('.overlay2');

const btnCloseModal = document.querySelector('.close-modal');
const btnCloseModal1 = document.querySelector('.close-modal1');



const btnOpenModal = document.querySelector('.show-modal');
const deleteProductButton = document.querySelector('.delete-product-button');
const for_delete_input = document.getElementById('for_delete_input');
const password = document.getElementById('password');

const openModal = function () {
    modal.classList.remove('hidden');
    overlay.classList.remove('hidden');
};

const deleteProduct = function () {
    modal1.classList.remove('hidden1');
    overlay1.classList.remove('hidden1');
};

//Измените описание!
const closeModal1 = function () {
    modal1.classList.add('hidden1');
    overlay1.classList.add('hidden1');
    for_delete_input.value = " ";
};
//Измените описание!

const closeModal = function () {
    console.log()
    modal.classList.add('hidden');
    overlay.classList.add('hidden');
    password.value = " ";
    containerModal.innerHTML = "";
};


// const closeModal3 = function () {
//     modal.classList.add('hidden');
//     overlay.classList.add('hidden');
//     password.value = " ";
//     containerModal.innerHTML = "";
// };


// for (let i = 0; i < btnsOpenModal.length; i++)
btnOpenModal.addEventListener('click', openModal);

//Измените описание!
deleteProductButton.addEventListener('click', deleteProduct);
btnCloseModal1.addEventListener('click', closeModal1);
//Измените описание!

btnCloseModal.addEventListener('click', closeModal);
// btnCloseModal2.addEventListener('click', closeModal2);
// overlay.addEventListener('click', closeModal);

document.addEventListener('keydown', function (e) {
    // console.log(e.key);

    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
        closeModal();
    }
});
// modal close

// const btnCloseModal3 = document.querySelector('.close-modal3');
// const closeModal3 = function () {
//     modal.classList.add('hidden');
//     overlay.classList.add('hidden');
//     password.value = " ";
//     containerModal.innerHTML = "";
// }
// btnCloseModal3.addEventListener('click', closeModal3);

let overlay10 = document.getElementById('overlay')

function closeModal3() {
    containerModal.classList.add('hidden');
    overlay10.classList.add('hidden');
    location.reload()
}

const containerModal = document.getElementById('containerModal');
const xhttp = new XMLHttpRequest();
const forInfoPass = document.getElementById('forInfoPass');
let url = window.location.href;
function OpenNewModal() {
    xhttp.open('POST', '/clients/my_products/info/' + url.substring(url.lastIndexOf('/') + 1), true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send(JSON.stringify({'password' : forInfoPass.value}));
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            const resp = JSON.parse(this.responseText);
            if (resp['data']['ap_password']) {
                containerModal.innerHTML = "<button class=\"close-modal3\" onclick=\"closeModal3()\">&times;</button>\n" +
                    "\n" +
                    "    <div class=\"header\">\n" +
                    "        <h2>Информация о товаре</h2>\n" +
                    "    </div>\n" +
                    "\n" +
                    "    <div class=\"form2\">\n" +
                    "        <div class=\"form-control\">\n" +
                    "            <label for=\"default_login\">Default Login</label>\n" +
                    "            <div id=\"default_login\" class=\"information\">" + resp['data']['def_login'] + "</div>\n" +
                    "\n" +
                    "            <label for=\"default_password\">Логин по умолчанию</label>\n" +
                    "            <div id=\"default_password\" class=\"information\">" + resp['data']['def_password'] + "</div>\n" +
                    "\n" +
                    "            <label for=\"ap_login\">Логин Ap</label>\n" +
                    "            <div id=\"ap_login\" class=\"information\">" + resp['data']['ap_login'] + "</div>\n" +
                    "\n" +
                    "            <label for=\"ap_password\">Пароль Ap</label>\n" +
                    "            <div id=\"ap_password\" class=\"information\">" + resp['data']['ap_password'] + "</div>\n" +
                    "        </div>\n" +
                    "\n" +
                    "    </div>"
            }
        }
    }
}
