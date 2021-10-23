var xhttp = new XMLHttpRequest();

function actionCommand(e) {
    let action = {
        'serial_num': e.getAttribute('ser_num'),
        'action_requested' : e.getAttribute('action'),
        'prefix' : 'socket'
    }
    xhttp.open('POST', '/clients/my_products/my_product/action', true);
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
    let x = ev.previousElementSibling.getAttribute("ser_num");
    window.open('/clients/my_products/my_product/' + x, '_self');
}

function Logout() {
    window.open('/clients/logout', '_self');
}

// modal open
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
    ser_num.value = "";
    desc.value = "";
};

const closeModal2 = function () {
    modal.classList.add('hidden');
    overlay.classList.add('hidden');
    ser_num.value = "";
    desc.value = "";
};
// for (let i = 0; i < btnsOpenModal.length; i++)
btnOpenModal.addEventListener('click', openModal);

btnCloseModal.addEventListener('click', closeModal);
btnCloseModal2.addEventListener('click', closeModal2);
// overlay.addEventListener('click', closeModal);

document.addEventListener('keydown', function (e) {

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

    btnCloseModal.addEventListener('click', function () {
        window.open('/', '_self');
    })

    btnCloseModal2.addEventListener('click', function () {
        window.open('/', '_self');
    })
}


const my_products_img = document.querySelectorAll('.my-products-img');
const  req_action = document.getElementsByClassName('ONOF');
window.addEventListener('load', function (){

let w;
    let serNums = [];
    let prefixes = [];
    for (let i=0; i < my_products_img.length; i++) {
        serNums.push(my_products_img[i].getAttribute('ser_num'));
        prefixes.push(my_products_img[i].getAttribute('prefix'));
    }
    let json = {
        'ser_nums': serNums,
        'prefixs': prefixes
    }
    if (typeof(Worker) !== "undefined") {
        if (typeof (w) == "undefined") {
            w = new Worker("/static/js/clients/socket_worker.js");
        }
        w.postMessage(json)
        w.onmessage = function (ev) {
            for (let i=0; i < my_products_img.length; i++) {
                for (let j in ev.data['data']) {
                    var key = j;
                    var val = ev.data['data'][j];
                    for (var a in val) {
                        var sub_key = a;
                        var sub_val = val[a];
                        if (my_products_img[i].getAttribute('ser_num') == sub_key) {
                            my_products_img[i].setAttribute('action', sub_val['state'])
                            let on_off;
                            if (sub_val['state'] == 'ON'){
                                on_off = 'Включен';
                            }
                            if(sub_val['state'] == 'OFF'){
                                on_off = 'Выключен';
                            }
                            req_action[i].style.backgroundColor = 'white';
                            req_action[i].innerHTML = on_off;

                        }
                    }
                }
            }
        };
    }

})


