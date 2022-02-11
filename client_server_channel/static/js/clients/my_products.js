var xhttp = new XMLHttpRequest();

function actionCommand(e) {
    let action = {
        'serial_num': e.getAttribute('ser_num'),
        'action_requested': e.getAttribute('action'),
        'prefix': 'socket'
    };
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

function socket3Way(e) {
    let action_inputs = e.parentNode.querySelectorAll('input');
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

function goSocket(ev) {
    let e = ev.previousElementSibling;
    let x = ev.previousElementSibling.getAttribute("ser_num");
    window.open('/clients/my_products/my_product/' + x, '_self');
    characterElement(e);
}

function Logout() {
    window.open('/clients/logout', '_self');
}

// modal open
const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.close-modal');
const btnCloseModalLocal = document.querySelector('.close-modal-localStorage');
const btnCloseModalLocal2 = document.querySelector('.close-modal3');
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

const closeModalLocal = function () {
    // modal.classList.add('hidden');
    // overlay.classList.add('hidden');
    window.history.back();
    ser_num.value = "";
    desc.value = "";
};

const closeModalLocal2 = function () {
    // modal.classList.add('hidden');
    // overlay.classList.add('hidden');
    window.history.back();
    ser_num.value = "";
    desc.value = "";
};

const closeModal2 = function () {
    modal.classList.add('hidden');
    overlay.classList.add('hidden');
    ser_num.value = "";
    desc.value = "";
};

btnOpenModal.addEventListener('click', openModal);
btnCloseModal.addEventListener('click', closeModal);
btnCloseModalLocal2.addEventListener('click', closeModalLocal2);
btnCloseModalLocal.addEventListener('click', closeModalLocal);
btnCloseModal2.addEventListener('click', closeModal2);

document.addEventListener('keydown', function (e) {

    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
        closeModal();
    }
});
// modal close

const my_products_img = document.querySelectorAll('.my-products-img');

function characterElement(e) {
    let serNum = e.getAttribute('ser_num');
    let state_time = e.getAttribute('state_time');

    let json = {
        'ser_num': serNum,
        'state_time': state_time
    };

    xhttp.open('POST', '/clients/my_products/update_prev_state', true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send(JSON.stringify(json));
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // let resp = JSON.parse(this.responseText);
            console.log(this.responseText);
        }
    }
}

function productImg(ev) {
    var x = ev.getAttribute("ser_num");
    window.open('/clients/my_products/my_product/' + x, '_self');
    characterElement(ev);
}

window.onload = function () {
    if (localStorage.getItem("openModal") == "open") {
        openModal();
        btnCloseModalLocal.style.display = 'block';
        btnCloseModalLocal2.style.display = 'block';
        btnCloseModal2.remove();
        btnCloseModal.remove();
        localStorage.removeItem('openModal');
    }
};

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

const parent_curr_state = document.getElementsByClassName('parent-curr-state');
const character = document.getElementsByClassName('character');
const socket3way_buttons = document.querySelectorAll('.socket3');

window.addEventListener('load', function () {
    let w;
    let serNums = [];
    let prefixes = [];
    let device_type = [];
    for (let i = 0; i < my_products_img.length; i++) {
        serNums.push(my_products_img[i].getAttribute('ser_num'));
        prefixes.push(my_products_img[i].getAttribute('prefix'));
        device_type.push(my_products_img[i].getAttribute('device_type'));
    }
    let json = {
        'ser_nums': serNums,
        'prefixs': prefixes,
        'device_type':device_type
    };
    if (typeof (Worker) !== "undefined") {
        if (typeof (w) == "undefined") {
            w = new Worker("/static/js/clients/socket_worker.js");
        }
        w.postMessage(json);
        w.onmessage = function (ev) {
            for (let i = 0; i < my_products_img.length; i++) {
                let id = my_products_img[i].getAttribute('id');
                for (let j in ev.data['data']) {
                    var key = j;
                    var val = ev.data['data'][j];
                    for (var a in val) {
                        var sub_key = a;
                        var sub_val = val[a];

                        if (my_products_img[i].getAttribute('ser_num') == sub_key) {
                            let ser_num = my_products_img[i].getAttribute('ser_num');

                            if (id == 10) {
                                let state_left = translateState(sub_val['state_left'], id);
                                let state_center = translateState(sub_val['state_center'], id);
                                let state_right = translateState(sub_val['state_right'], id);
                                parent_curr_state[i].innerHTML = "<span class='curr-state-left state-all' style='background-color: " + state_left['bg_Color'] + "'>" + state_left['state'] + "</span>" +
                                    "<span class='curr-state-center state-all' style='background-color: " + state_center['bg_Color'] + "'>" + state_center['state'] + "</span>" +
                                    "<span class='curr-state-right state-all' style='background-color: " + state_right['bg_Color'] + "'>" + state_right['state'] + "</span>";
                                let left_value = decTranslateState(sub_val['state_left']);
                                let center_value = decTranslateState(sub_val['state_center']);
                                let right_value = decTranslateState(sub_val['state_right']);
                                let state_all = document.getElementsByClassName('state-all');

                                for (let i = 0; i < socket3way_buttons.length; i++) {
                                    if (state_all[i].innerText == state_left['state']) {
                                        socket3way_buttons[i].innerHTML = left_value;
                                        socket3way_buttons[i].attributes[1].value = sub_val['state_left'];
                                    }
                                    if (state_all[i].innerText == state_center['state']) {
                                        socket3way_buttons[i].innerHTML = center_value;
                                        socket3way_buttons[i].attributes[1].value = sub_val['state_center'];
                                    }
                                    if (state_all[i].innerText == state_right['state']) {
                                        socket3way_buttons[i].innerHTML = right_value;
                                        socket3way_buttons[i].attributes[1].value = sub_val['state_right'];
                                    }
                                }

                            } else if(id == 11){
                                if (getFullTime(sub_val['action_time'])  == '-' || getFullTime(sub_val['action_time'])  == 'ISO.undefined.0 0' || getFullTime(sub_val['action_time'])  == '0.undefined.0 0') {
                                    parent_curr_state[i].innerHTML = "";
                                    parent_curr_state[i].style.backgroundColor = 'transparent';
                                } else if (sub_val['action_taken'] == "YES"){
                                    parent_curr_state[i].innerHTML = getFullTime(sub_val['action_time']);
                                    parent_curr_state[i].style.backgroundColor = 'green';
                                    parent_curr_state[i].style.color = 'white';
                                }

                            } else {
                                let state = translateState(sub_val['state'], id);
                                parent_curr_state[i].innerHTML = "<span class='curr-state' style='background-color: " + state['bg_Color'] + "'>" + state['state'] + "</span>";
                            }

                            my_products_img[i].setAttribute('state_time', sub_val['state_change_time']);


                            if (getFullTime(sub_val['state_change_time']) > getFullTime(sub_val['prev_state_time'])) {
                                character[i].innerHTML = '!';
                                character[i].style.display = 'inline-block';
                            }else {
                                character[i].innerHTML = '';
                                character[i].style.display = 'none';
                            }
                        }
                    }
                }
            }
        };
    }

})


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
        if (state != "ON" && state != "OFF") {
            return {
                'bg_Color': 'transparent',
                'state': ''
            }
        }
    } else if (id == 5){  // suv datchik
        if (state == "ON") {
            return {
                'bg_Color': 'red',
                'state': 'Вода капала'
            }
        }
        if (state == "OFF") {
            return {
                'bg_Color': 'green',
                'state': 'Сухой'
            }
        }
    }else if (id == 9){  // invertor
        if (state == "ON") {
            return {
                'bg_Color': 'red',
                'state': 'Внутренний питания'
            }
        }
        if (state == "OFF") {
            return {
                'bg_Color': 'green',
                'state': 'Внешнее питание'
            }
        }
    } else if (id == 7){  // invertor
        if (state == "ON") {
            return {
                'bg_Color': 'red',
                'state': 'Обнаружен дым'
            }
        }
        if (state == "OFF") {
            return {
                'bg_Color': 'green',
                'state': 'Дым не обнаружен'
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
        if (state != "ON" && state != "OFF") {
            return {
                'bg_Color': 'transparent',
                'state': ''
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