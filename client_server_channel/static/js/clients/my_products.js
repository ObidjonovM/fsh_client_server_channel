var xhttp = new XMLHttpRequest();

function actionCommand(e) {
    let action = {
        'serial_num': e.getAttribute('ser_num'),
        'action_requested' : e.getAttribute('action')
    }
    xhttp.open('POST', '/clients/my_products/socket/action', true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send(JSON.stringify(action));
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // let resp = JSON.parse(this.responseText);
            console.log(this.responseText)
        }
    }
}


function goSocket(ev){
    let x = ev.previousElementSibling.getAttribute("ser_num2");
    window.open('/clients/my_products/socket/' + x, '_self');
}

function Logout() {
    window.open('/clients/logout', '_self');
}

// modal open
'use strict';

const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.close-modal');
const btnCloseModal2 = document.querySelector('.close-modal2');
const btnOpenModal = document.querySelector('.show-modal');
const ser_num = document.getElementById('ser_num');
const desc = document.getElementById('desc');

const openModal = function () {
    modal.classList.remove('hidden');
    overlay.classList.remove('hidden');
};

const closeModal = function () {
    modal.classList.add('hidden');
    overlay.classList.add('hidden');
    ser_num.value = " ";
    desc.value = " ";
};

const closeModal2 = function () {
    modal.classList.add('hidden');
    overlay.classList.add('hidden');
    ser_num.value = " ";
    desc.value = " ";
};
// for (let i = 0; i < btnsOpenModal.length; i++)
btnOpenModal.addEventListener('click', openModal);

btnCloseModal.addEventListener('click', closeModal);
btnCloseModal2.addEventListener('click', closeModal2);
// overlay.addEventListener('click', closeModal);

document.addEventListener('keydown', function (e) {
    // console.log(e.key);

    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
        closeModal();
    }
});

// modal close


function productImg(ev) {

    var x = ev.getAttribute("ser_num");
    window.open('/clients/my_products/my_product/' + x, '_self');
}

window.onload = function () {
    if (localStorage.getItem("openModal") == "open") {
        openModal();
        localStorage.removeItem('openModal');
    }
}



var w;

window.addEventListener('load', function (){

    if (typeof(Worker) !== "undefined") {
        if (typeof (w) == "undefined") {
            w = new Worker("/static/js/clients/socket_worker.js");
        }
        w.onmessage = function (ev) {
            console.log(ev.data)
        };
    }

})


