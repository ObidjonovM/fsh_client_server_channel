var xhttp = new XMLHttpRequest();

function actionCommand(e) {
    let action = {
        'serial_num': e.getAttribute('ser_num'),
        'action_requested': e.getAttribute('action'),
        'prefix': 'socket'
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


// modal open
//Delete my product open!
const overlay1 = document.querySelector('.overlay1');
const modal1 = document.querySelector('.modal1');
const btnCloseModal1 = document.querySelector('.close-modal1');
const deleteProductButton = document.querySelector('.delete-product-button');
const for_delete_input = document.getElementById('for_delete_input');
const delete_form = document.getElementById('delete_form');

const closeModal1 = function () {
    modal1.classList.add('hidden1');
    overlay1.classList.add('hidden1');
    for_delete_input.value = "";
};

const deleteProduct = function () {
    modal1.classList.remove('hidden1');
    overlay1.classList.remove('hidden1');
};

deleteProductButton.addEventListener('click', deleteProduct);
btnCloseModal1.addEventListener('click', closeModal1);
//Delete my product close!


//information about my product open
const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const forInfoPass = document.getElementById('forInfoPass');
const btnCloseModalInformation = document.querySelector('.close-modal');
const btnOpenModal = document.querySelector('.show-modal');

const openModal = function () {
    modal.classList.remove('hidden');
    overlay.classList.remove('hidden');
};

const closeModalInformation = function () {
    forInfoPass.value = "";
    modal.classList.add('hidden');
    overlay.classList.add('hidden');
};

// for (let i = 0; i < btnsOpenModal.length; i++)
btnOpenModal.addEventListener('click', openModal);
btnCloseModalInformation.addEventListener('click', closeModalInformation);
// btnCloseModal2.addEventListener('click', closeModal2);
// overlay.addEventListener('click', closeModal);

document.addEventListener('keydown', function (e) {
    // console.log(e.key);

    if (e.key === 'Escape' && !modal.classList.contains('hidden1')) {
        closeModal1();
    }
});
//information about my product close
// modal close


let overlay10 = document.getElementById('overlay');

function closeModal3() {
    containerModal.classList.add('hidden');
    overlay10.classList.add('hidden');
    location.reload()
}

const containerModal = document.getElementById('containerModal');
let url = window.location.href;

function OpenNewModal() {
    xhttp.open('POST', '/clients/my_products/my_product/info/' + url.substring(url.lastIndexOf('/') + 1), true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send(JSON.stringify({'password': forInfoPass.value}));
    console.log(forInfoPass.value)
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let resp = JSON.parse(this.responseText);
            if (resp['data']['ap_password']) {
                containerModal.innerHTML = "<button class=\"close-modal3" +
                    "\" onclick=\"closeModal3()\">&times;</button>\n" +
                    "\n" +
                    "    <div class=\"header\">\n" +
                    "        <h2>Информация о товаре</h2>\n" +
                    "    </div>\n" +
                    "\n" +
                    "    <div class=\"form2\">\n" +
                    "        <div class=\"form-control\">\n" +
                    "            <label for=\"default_login\">Логин по умолчанию</label>\n" +
                    "            <div id=\"default_login\" class=\"information\">" + resp['data']['def_login'] + "</div>\n" +
                    "\n" +
                    "            <label for=\"default_password\">Пароль по умолчанию</label>\n" +
                    "            <div id=\"default_password\" class=\"information\">" + resp['data']['def_password'] + "</div>\n" +
                    "\n" +
                    "            <label for=\"ap_login\">Логин устройство</label>\n" +
                    "            <div id=\"ap_login\" class=\"information\">" + resp['data']['ap_login'] + "</div>\n" +
                    "\n" +
                    "            <label for=\"ap_password\">Пароль устройство</label>\n" +
                    "            <div id=\"ap_password\" class=\"information\">" + resp['data']['ap_password'] + "</div>\n" +
                    "        </div>\n" +
                    "\n" +
                    "    </div>"
            }
        }
    }
}

document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
        closeModalInformation();
    }
});

document.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') {
        OpenNewModal();
    }
})


// All time open
function addZero(e) {
    let result = ""
    if (e.length < 2) {
        result = "0" + e
    } else {
        result = e
    }
    return result
}

const monthName = {
    'Jan': '01', 'Feb': '02', 'Mart': '03',
    'Apr': '04', 'May': '05', 'Jun': '06',
    'Jul': '07', 'Aug': '08', 'Sep': '09',
    'Oct': '10', 'Nov': '11', 'Dec': '12'
};

function getFullTime(fullTime) {
    let month = fullTime.substring(fullTime.indexOf(" ", 5) + 1, fullTime.indexOf(" ", 9));
    let day = fullTime.substring(fullTime.indexOf(" ") + 1, fullTime.indexOf(" ", 5));
    let year = fullTime.substring(fullTime.indexOf(" ", 9) + 1, fullTime.indexOf(" ", 14));
    let hours = fullTime.substring(fullTime.indexOf(" ", 14) + 1, fullTime.indexOf(" ", 22));

    let dmyh = addZero(day) + "." + monthName[month] + "." + addZero(year) + " " + addZero(hours);

    return dmyh;
}


const all_time_input2 = document.getElementById('all_time_input');
window.addEventListener('load', function () {

    let w1;
    let json = {
        'ser_num': all_time_input2.getAttribute('ser_num'),
        'prefix': all_time_input2.getAttribute('prefix')
    };

    if (typeof (Worker) !== "undefined") {
        if (typeof (w1) == "undefined") {
            w1 = new Worker("/static/js/clients/s_worker2.js");
        }
        w1.postMessage(json)

        w1.onmessage = function (ev) {
            // console.log(ev.data['request_time']);
            // || getFullTime(ev.data['request_time']) == 'ISO.undefined.0 0'
            if (getFullTime(ev.data['request_time']) == '-' || getFullTime(ev.data['request_time']) == 'ISO.undefined.0 0' || getFullTime(ev.data['request_time']) == '0.undefined.0 0') {
                all_time_input2.innerHTML = '';
                all_time_input2.style.border = 'none';
                all_time_input2.style.outline = 'none';
            } else {
                all_time_input2.innerHTML = getFullTime(ev.data['request_time']);
                // all_time_input2.style.border = '1px solid #b8bbb8';
                // console.log(getFullTime(ev.data['request_time']));
            }
        };
    }

})
// All time close


// Дата начала and Дата окончания open
function sendData() {

    const data_form = document.getElementById('data_form');
    const ser_number = data_form.getAttribute('ser_num');
    const prefix = document.getElementById('hidden_input2');
    const start_date = document.getElementById('start_date').value;
    const end_date = document.getElementById('end_date').value;
    const tbody_date = document.getElementById('tbody_date');

    const json = {
        'prefix': prefix.getAttribute('value'),
        'start_date': start_date+'T00:00',
        'end_date': end_date+'T23:59'
    };

    xhttp.open("Post", "/clients/my_products/my_product/logs/" + ser_number);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send(JSON.stringify(json));

    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let resp = JSON.parse(this.responseText);
            for (let i = resp['data']['state'].length-1; i >= 0;  i--) {

                let tr = document.createElement('TR');
                tr.setAttribute('id', 'tbody_tr');

                let td1 = document.createElement('TD');
                let td2 = document.createElement('TD');

                td1.setAttribute('id', 'state_time_on_of');
                td2.setAttribute('id', 'state_time_on_of');

                td1.innerHTML = resp['data']['state'][i];
                td2.innerHTML = getFullTime(resp['data']['state_time'][i]);

                tr.appendChild(td1);
                tr.appendChild(td2);

                tbody_date.appendChild(tr);

            }
        }
    }
}

const form = document.getElementById("data_form");

form.addEventListener("submit", function (event) {
    event.preventDefault();

    sendData();
    open3();
});

const modal3 = document.querySelector('.modal3');
const overlay3 = document.querySelector('.overlay3');
const close_modal4 = document.querySelector('.close-modal4');
const date_submit = document.getElementById('date_submit');
const state_time_on_of = document.getElementById('state_time_on_of');
const table_date = document.querySelector('.table-date');

const open3 = function () {
    modal3.classList.remove('hidden3');
    overlay3.classList.remove('hidden3');
};

const closeModal5 = function () {
    modal3.classList.add('hidden3');
    overlay3.classList.add('hidden3');
    location.reload();

};

date_submit.addEventListener('submit', open3);
close_modal4.addEventListener('click', closeModal5);
// Дата начала and Дата окончания close


//ON OF open
const socket_img = document.querySelectorAll('.socket-img');
const req_action = document.getElementsByClassName('ONOF');
let id = socket_img[0].getAttribute('id');
let character = document.getElementById('character_id');
let characters = document.getElementsByClassName('character12');

function characterOtmen(e) {
    let  serNum = e.getAttribute('ser_num');
    let  state_time = e.getAttribute('state_time');
    let json = {
        'ser_num':serNum,
        'state_time': state_time
    }

    xhttp.open('POST', '/clients/my_products/update_prev_state', true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send(JSON.stringify(json));
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // let resp = JSON.parse(this.responseText);
            console.log(this.responseText)
        }
    }
}


window.addEventListener('load', function () {

    let w;
    let serNum = '';
    let prefix = '';
    // for (let i=0; i < socket_img.length; i++) {
    serNum = socket_img[0].getAttribute('ser_num');
    prefix = socket_img[0].getAttribute('prefix');
    // }
    let json = {
        'ser_num': serNum,
        'prefix': prefix
    };
    if (typeof (Worker) !== "undefined") {
        if (typeof (w) == "undefined") {
            w = new Worker("/static/js/clients/s_worker.js");
        }
        w.postMessage(json)

        w.onmessage = function (ev) {
            let on_of;
            for (let i = 0; i < req_action.length; i++) {
                characters[i].setAttribute('state_time', ev.data['state_change_time']);
                if (ev.data['notification'] === 'YES'){
                    characters[i].innerHTML = 'x';
                    characters[i].style.display = 'inline-block';
                }

                if (ev.data['notification'] === 'NO'){
                    characters[i].innerHTML = '';
                    characters[i].style.display = 'none';
                }

                if (ev.data['state'] == 'ON') {
                    on_of = 'Включен';
                    req_action[i].style.backgroundColor = 'green';
                    req_action[i].style.color = 'white';
                }
                if (ev.data['state'] == 'OFF') {
                    on_of = 'Выключен';
                    req_action[i].style.backgroundColor = 'red';
                    req_action[i].style.color = 'white';
                }
                if ((ev.data['state'] == 'ON' && id == 4) || (ev.data['state'] == 'ON' && id == 8)) {
                    on_of = 'Закрыто';
                    req_action[i].style.backgroundColor = 'green';
                    req_action[i].style.color = 'white';
                }
                if ((ev.data['state'] == 'OFF' && id == 4) || (ev.data['state'] == 'OFF' && id == 8)) {
                    on_of = 'Открыто';
                    req_action[i].style.backgroundColor = 'red';
                    req_action[i].style.color = 'white';
                }
                req_action[i].innerHTML = on_of;
                if (ev.data['state'] == 'undefined' || ev.data['state'] == '-') {
                     req_action[i].style.backgroundColor = 'transparent';
                     req_action[i].textContent = '';
                }

            }
        };
    }

});
//ON OF close


//get my products open
function myProducts() {
    window.open('/clients/my_products', '_self');
}

//get my products close
