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
            if (getFullTime(ev.data['request_time']) == '-' || getFullTime(ev.data['request_time']) == 'ISO.undefined.0 0' || getFullTime(ev.data['request_time']) == '0.undefined.0 0') {
                all_time_input2.innerHTML = '';
                all_time_input2.style.border = 'none';
                all_time_input2.style.outline = 'none';
            } else {
                all_time_input2.innerHTML = getFullTime(ev.data['request_time']);
                // console.log(getFullTime(ev.data['request_time']));
            }
        };
    }

})
// All time close


// Дата начала and Дата окончания open
const socket_img = document.querySelectorAll('.socket-img');
const id = socket_img[0].getAttribute('id');
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

                if (id == 8 || id == 10){
                    if (resp['data']['state'][i] == 'ON') {
                        td1.innerHTML = "Открыто";
                    }

                    if (resp['data']['state'][i] == 'OFF') {
                        td1.innerHTML = "Закрыто";
                    }
                }else {
                    if (resp['data']['state'][i] == 'ON') {
                        td1.innerHTML = "Включен";
                    }

                    if (resp['data']['state'][i] == 'OFF') {
                        td1.innerHTML = "Выключен";
                    }
                }

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

function socket3Way(e) {
    let action = {
        'serial_num': e.getAttribute('ser_num'),
        'prefix': 'socket3x'
    };

    if (e.hasAttribute('action_left')) {
        action['action_requested_left'] = reverseState(e.getAttribute('action_left'));
    }
    if (e.hasAttribute('action_center')) {
        action['action_requested_center'] = reverseState(e.getAttribute('action_center'));
    }
    if (e.hasAttribute('action_right')) {
        action['action_requested_right'] = reverseState(e.getAttribute('action_right'));
    }


    xhttp.open('POST', '/clients/my_products/my_product/action', true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send(JSON.stringify(action));
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let resp = JSON.parse(this.responseText);
            console.log(resp)
        }
    }
}

//ON OF open
// const req_action = document.getElementsByClassName('ONOF');
const parent_curr_state = document.getElementsByClassName('parent-curr-state');
let character = document.getElementById('character_id');
let characters = document.getElementsByClassName('character12');
const socket3way_buttons = document.querySelectorAll('.socket3');

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
            for (let i = 0; i < parent_curr_state.length; i++) {
                characters[i].setAttribute('state_time', ev.data['state_change_time']);

                if (getFullTime(ev.data['state_change_time']) > getFullTime(ev.data['prev_state_time']) ){
                    characters[i].innerHTML = 'x';
                    characters[i].style.display = 'inline-block';
                }else {
                    characters[i].innerHTML = '';
                    characters[i].style.display = 'none';
                }

                if (id == 10) {
                    let state_left = translateState(ev.data['state_left'], id);
                    let state_center = translateState(ev.data['state_center'], id);
                    let state_right = translateState(ev.data['state_right'], id);
                    parent_curr_state[i].innerHTML = "<span class='curr-state-left state-all' style='background-color: " + state_left['bg_Color'] + "'>" + state_left['state'] + "</span>" +
                        "<span class='curr-state-center state-all' style='background-color: " + state_center['bg_Color'] + "'>" + state_center['state'] + "</span>" +
                        "<span class='curr-state-right state-all' style='background-color: " + state_right['bg_Color'] + "'>" + state_right['state'] + "</span>";
                    let left_value = decTranslateState(ev.data['state_left']);
                    let center_value = decTranslateState(ev.data['state_center']);
                    let right_value = decTranslateState(ev.data['state_right']);
                    let state_all = document.getElementsByClassName('state-all');

                    for (let i = 0; i < socket3way_buttons.length; i++) {
                        if (state_all[i].innerText == state_left['state']) {
                            socket3way_buttons[i].innerHTML = left_value;
                            socket3way_buttons[i].attributes[1].value = ev.data['state_left'];
                        }
                        if (state_all[i].innerText == state_center['state']) {
                            socket3way_buttons[i].innerHTML = center_value;
                            socket3way_buttons[i].attributes[1].value = ev.data['state_center'];
                        }
                        if (state_all[i].innerText == state_right['state']) {
                            socket3way_buttons[i].innerHTML = right_value;
                            socket3way_buttons[i].attributes[1].value = ev.data['state_right'];
                        }
                    }

                    // input_on_off[i].innerHTML = "<input type=\"button\" action_left=\""+ sub_val['state_left'] +"\" value=\""+ left_value +"\" onclick=\"socket3Way(this)\" class=\"on\"\n" +
                    //     "                               ser_num=\""+ ser_num +"\">\n" +
                    //     "\n" +
                    //     "                        <input type=\"button\" action_center=\""+ sub_val['state_center'] +"\" value=\"" +center_value+ "\" onclick=\"socket3Way(this)\" class=\"off\"\n" +
                    //     "                               ser_num=\""+ser_num+"\">\n" +
                    //     "\n" +
                    //     "                        <input type=\"button\" action_right=\""+ sub_val['state_right'] +"\" value=\""+right_value+"\" onclick=\"socket3Way(this)\" class=\"off\"\n" +
                    //     "                               ser_num=\""+ser_num+"\">";
                } else {
                    let state = translateState(ev.data['state'], id);
                    parent_curr_state[i].innerHTML = "<span class='curr-state' style='background-color: " + state['bg_Color'] + "'>" + state['state'] + "</span>";
                }

            }
        };
    }

});
//ON OF close

function translateState(state, id) {
    if (id == 4 || id == 8) {
        if (state == "ON") {
            return {
                'bg_Color': 'green',
                'state': 'Закрыто'
            }
        }
        if (state == "OFF") {
            return {
                'bg_Color': 'red',
                'state': 'Открыто'
            }
        }
    } else {
        if (state == "ON") {
            return {
                'bg_Color': 'green',
                'state': 'Включен'
            }
        }
        if (state == "OFF") {
            return {
                'bg_Color': 'red',
                'state': 'Выключен'
            }
        }
    }
}

function decTranslateState(state) {
    if (state == "ON") {
        return 'Выключить';
    } else {
        return 'Включить';
    }
}

function reverseState(state) {
    if (state == "ON") {
        return 'OFF';
    }
    if (state == "OFF") {
        return 'ON';
    }
}


//get my products open
function myProducts() {
    window.open('/clients/my_products', '_self');
}
//get my products close

// tuvak open
function Tuvak(e) {

    json = {

    }

    xhttp.open('POST', '', true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send(JSON.stringify());
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // let resp = JSON.parse(this.responseText);
            console.log(this.responseText);
        }
    }

}
// tuvak close


function changeInput() {
    var fistDate1 = document.getElementById('start_date').value;
    document.getElementById('end_date').value = fistDate1;
}
