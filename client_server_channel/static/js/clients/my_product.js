var xhttp = new XMLHttpRequest();

function actionCommand(e) {
    let prefix = e.getAttribute('prefix');
    let action = {
        'serial_num': e.getAttribute('ser_num'),
        'action_requested': e.getAttribute('action'),
        'prefix': prefix
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
const btnOpenModal = document.querySelector('.show-modal');

const openModal = function () {
    modal.classList.remove('hidden');
    overlay.classList.remove('hidden');
};

btnOpenModal.addEventListener('click', openModal);
// btnCloseModalInformation.addEventListener('click', closeModalInformation);

document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && !modal.classList.contains('hidden1')) {
        closeModal1();
    }
});
//information about my product close
// modal close

function locationReload() {
    window.location.reload();
}

let overlay10 = document.getElementById('overlay');

function closeModal3() {
    containerModal.classList.add('hidden');
    overlay10.classList.add('hidden');
    locationReload();
}

// Подключите устройство к Интернету open

const containerModal = document.getElementById('containerModal');
let url = window.location.href;
let product_id;

window.addEventListener('load', function () {

// media and kom uchun alohida js open

    xhttp.open('POST', "/clients/my_products/my_product/info/" + url.substring(url.lastIndexOf('/') + 1), true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send();

    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let resp = JSON.parse(this.responseText);
            product_id = resp['data']['product_id'];

            function configurationFunction(x) {
                if (x.matches) {
                    containerModal.innerHTML = " <button class=\"close-modal" +
                        "\" onclick=\"closeModal3()\">&times;</button>\n" +
                        "        <div class=\"slidercontainer\">\n" +

                        "            <div class=\"showSlide fade\">\n" +
                        "                <img src=\"/static/img/3/gaz1.png\"/>\n" +
                        "                <div class=\"content\">1.1 - Gaz Datchikni to'kka ulang.</div>\n" +
                        "            </div>\n" +
                        "\n" +

                        "            <div class=\"showSlide fade\">\n" +
                        "                <img src=\"/static/img/3/gaz2.jpg\"/>\n" +
                        "                <div class=\"content\"><b>1.2 - Gaz Datchikni ko'rsatilganidek bir marta bosing.</b></div>\n" +
                        "            </div>\n" +
                        "\n" +
                        "            <div class=\"showSlide fade\">\n" +
                        "                <img src=\"/static/img/3/gaz3.jpg\"/>\n" +
                        "                <div class=\"content\"><b>1.3 - Gaz Datchik o'zidan wifi tarqatish uchun bosiladigan joy.</b></div>\n" +
                        "            </div>\n" +
                        "\n" +
                        "            <div class=\"showSlide fade\">\n" +
                        "                <img src=\"/static/img/3/gaz4.jpg\"/>\n" +
                        "                <div class=\"content\"><b>1.4 - Gaz Datchikda ko'rsatilgan joyni 10 sekund mobaynida bosib turing.</b></div>\n" +
                        "            </div>\n" +
                        "\n" +
                        "            <div class=\"showSlide fade\">\n" +
                        "                <img src=\"/static/img/wifi_connect_img/tel1.jpg\" class=\"tel\"/>\n" +
                        "                <div class=\"content\"><b>2.1 - Productingizni wifiyiga telfon orqali ulanish.</b></div>\n" +
                        "            </div>\n" +
                        "\n" +
                        "            <div class=\"showSlide fade\">\n" +
                        "                <img src=\"/static/img/wifi_connect_img/tel2.jpg\" class=\"tel\"/>\n" +
                        "                <div class=\"content\"><b>2.2 - Wifi tugmani bosib turish orqali wifiyingiz sozlamalariga kirasiz.</b></div>\n" +
                        "            </div>\n" +
                        "\n" +
                        "            <div class=\"showSlide fade\">\n" +
                        "                <img src=\"/static/img/wifi_connect_img/tel3.jpg\" class=\"tel\"/>\n" +
                        "                <div class=\"content\"><b>2.3 - Bu yerdan wifiyingizni actual xolatga o'tkazasiz, ya'ni wifiyingizni\n" +
                        "                    yoqasiz.</b>\n" +
                        "                </div>\n" +
                        "            </div>\n" +
                        "\n" +
                        "            <div class=\"showSlide fade\">\n" +
                        "                <img src=\"/static/img/wifi_connect_img/tel4.jpg\" class=\"tel\"/>\n" +
                        "                <div class=\"content\"><b>2.4 - Wifiyingizni yoqganingizdan so'ng bir qator wifi nomlari chiqadi.</b></div>\n" +
                        "            </div>\n" +
                        "\n" +
                        "            <div class=\"showSlide fade\">\n" +
                        "                <img src=\"/static/img/wifi_connect_img/tel5.jpg\" class=\"tel\"/>\n" +
                        "                <div class=\"content\"><b>2.5 - Wifi nomlari orasidan " + resp['data']['ap_login'] + "  nomli wifiga ulanasiz.</b></div>\n" +
                        "            </div>\n" +
                        "\n" +
                        "            \n" +
                        "            <a class=\"left\" onclick=\"nextSlide(-1)\">Prev</a>\n" +
                        "            <a class=\"right\" onclick=\"nextSlide(1)\">Next</a>\n" +
                        "        </div>";
                } else {
                    containerModal.innerHTML = " <button class=\"close-modal" +
                        "\" onclick=\"closeModal3()\">&times;</button>\n" +
                        "        <div class=\"slidercontainer\">\n" +
                        "            <div class=\"showSlide fade\">\n" +
                        "                <img src=\"/static/img/3/gaz1.png\"/>\n" +
                        "                <div class=\"content\"><b>1.1 - Gaz Datchikni to'kka ulang.</b></div>\n" +
                        "            </div>\n" +
                        "\n" +
                        "            <div class=\"showSlide fade\">\n" +
                        "                <img src=\"/static/img/3/gaz2.jpg\"/>\n" +
                        "                <div class=\"content\"><b>1.2 - Gaz Datchikni ko'rsatilganidek bir marta bosing.</b></div>\n" +
                        "            </div>\n" +
                        "\n" +
                        "            <div class=\"showSlide fade\">\n" +
                        "                <img src=\"/static/img/3/gaz3.jpg\"/>\n" +
                        "                <div class=\"content\"><b>1.3 - Gaz Datchik o'zidan wifi tarqatish uchun bosiladigan joy.</b></div>\n" +
                        "            </div>\n" +
                        "\n" +
                        "            <div class=\"showSlide fade\">\n" +
                        "                <img src=\"/static/img/3/gaz4.jpg\"/>\n" +
                        "                <div class=\"content\"><b>1.4 - Gaz Datchikda ko'rsatilgan joyni <span style='color: purple; border:1px solid purple; padding: 3px; font-weight: bold'>10</span> sekund mobaynida bosib turing.</b></div>\n" +
                        "            </div>\n" +
                        "\n" +
                        "            <div class=\"showSlide fade\">\n" +
                        "                <img src=\"/static/img/wifi_connect_img/kom1.jpg\" class=\"kom\"/>\n" +
                        "                <div class=\"content kom\"><b>2.1 - Productingizni wifiyiga kompyuter orqali ulanish.</b></div>\n" +
                        "            </div>\n" +
                        "\n" +
                        "            <div class=\"showSlide fade\">\n" +
                        "                <img src=\"/static/img/wifi_connect_img/kom2.jpg\" class=\"kom\"/>\n" +
                        "                <div class=\"content kom\"><b>2.2 - Kompyuteringizni wifi tugmasini bir marta bosish orqali, wifi nomlarini\n" +
                        "                    ko'rishingiz mumkin.</b>\n" +
                        "                </div>\n" +
                        "            </div>\n" +
                        "\n" +
                        "            <div class=\"showSlide fade\">\n" +
                        "                <img src=\"/static/img/wifi_connect_img/kom3.jpg\" class=\"kom\"/>\n" +
                        "                <div class=\"content kom\"><b>2.3 - Bu yerdan <span style='color: #0c5460'>" + resp['data']['ap_login'] + "</span> nomli wifiga ulanasiz.</b></div>\n" +
                        "            </div>\n" +
                        "            \n" +
                        "            <div class=\"showSlide fade\">\n" +
                        "                <img src=\"/static/img/wifi_connect_img/kom4.jpg\" class=\"kom\"/>\n" +
                        "                <div class=\"content kom\"><b>2.3 - FidoElectronics... nomli wifiga ulangandan so'ng, kompyuteringizga Set (inetrnet) ulangan bo'lsa uzib qo'ying va 'Next' tugmasini bosing.</b></div>\n" +
                        "            </div>\n" +
                        "            <a class=\"left\" onclick=\"nextSlide(-1)\">Prev</a>\n" +
                        "            <a class=\"right\" onclick=\"nextSlide(1)\">Next</a>\n" +
                        "        </div>";
                }

            }

            const mmObj = window.matchMedia("(max-width: 1000px)");

            configurationFunction(mmObj);

            mmObj.addListener(configurationFunction);

        }
    }
// media and kom uchun alohida js close

});

var slide_index = 1;

function nextSlide(n) {
    displaySlides(slide_index += n);
}

function currentSlide(n) {
    displaySlides(slide_index = n);
}

function displaySlides(n) {
    var i;
    var slides = document.getElementsByClassName("showSlide");
    var aleft = document.querySelector('.left');

    if (n >= slides.length) {
        window.open("http://192.168.4.1", '_blank',
            'toolbar=yes,scrollbars=yes,resizable=yes,top=center,left=center');
        closeModal3();
    }

    if (n < 1) {
        slide_index = slides.length;
        aleft.style.pointerEvents = 'none';
        aleft.style.color = 'red';
        aleft.style.opacity = '.7';
        aleft.style.border = '1px solid red';
    }

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
        slides[slide_index - 1].style.display = "block";
    }

}

// Подключите устройство к Интернету close


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
    'Jan': '01', 'Feb': '02', 'Mar': '03',
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
            }
        };
    }

})
// All time close

// Дата начала and Дата окончания open
const socket_img = document.querySelectorAll('.socket-img');
const device_type = socket_img[0].getAttribute('device_type');
const id = socket_img[0].getAttribute('id');
const tbody_date = document.getElementById('tbody_date');
const tbody_date1 = document.getElementById('tbody_date1');
const tbody_date2 = document.getElementById('tbody_date2');

function sendData() {
    const start_date = document.getElementById('start_date').value;
    const end_date = document.getElementById('end_date').value;
    const data_form = document.getElementById('data_form');
    const ser_number = data_form.getAttribute('ser_num');
    const prefix = document.getElementById('hidden_input2');

    const json = {
        'prefix': prefix.getAttribute('value'),
        'start_date': start_date + 'T00:00',
        'end_date': end_date + 'T23:59',
        'device_type': device_type
    };

    xhttp.open("Post", "/clients/my_products/my_product/logs/" + ser_number);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send(JSON.stringify(json));

    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let resp = JSON.parse(this.responseText);

            for (let i = 0; i < resp['data']['log_id'].length; i++) {

                let tr = document.createElement('TR');
                tr.setAttribute('id', 'tbody_tr');

                let td1 = document.createElement('TD');
                let td2 = document.createElement('TD');

                td1.setAttribute('class', 'state_time_on_of');
                td2.setAttribute('class', 'state_time_on_of');

                if (id == 11) {
                    td1.innerHTML = resp['data']['action_requested'][i];
                    td2.innerHTML = getFullTime(resp['data']['action_time'][i]);
                } else {
                    td1.innerHTML = resp['data']['state'][i];
                    td2.innerHTML = getFullTime(resp['data']['state_time'][i]);
                }

                if (id == 8 || id == 10) {
                    if (resp['data']['state'][i] == 'ON') {
                        td1.innerHTML = "Открыто";
                    }

                    if (resp['data']['state'][i] == 'OFF') {
                        td1.innerHTML = "Закрыто";
                    }
                } else if (id == 11) {
                    if (resp['data']['action_requested'][i] == 'ON') {
                        td1.innerHTML = "Налил воду";
                    }
                } else {
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
const modal_flower = document.querySelector('.modal4');
const overlay_flower = document.querySelector('.overlay4');
const close_modal_flower = document.querySelector('.close-modal5');

const openFlower = function () {
    modal_flower.classList.remove('hidden4');
    overlay_flower.classList.remove('hidden4');
};

const closeModalFlower = function () {
    modal_flower.classList.add('hidden4');
    overlay_flower.classList.add('hidden4');
    location.reload();
};

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
close_modal_flower.addEventListener('click', closeModalFlower);

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
const parent_curr_state = document.getElementsByClassName('parent-curr-state');
let character = document.getElementById('character_id');
let characters = document.getElementsByClassName('character12');
const socket3way_buttons = document.querySelectorAll('.socket3');

function characterOtmen(e) {
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
            console.log(this.responseText)
        }
    }
}

window.addEventListener('load', function () {

    let w;
    let serNum = '';
    let prefix = '';
    let device_type = '';
    // for (let i=0; i < socket_img.length; i++) {
    serNum = socket_img[0].getAttribute('ser_num');
    prefix = socket_img[0].getAttribute('prefix');
    device_type = socket_img[0].getAttribute('device_type');
    // }
    let json = {
        'ser_num': serNum,
        'prefix': prefix,
        'device_type': device_type
    };
    if (typeof (Worker) !== "undefined") {
        if (typeof (w) == "undefined") {
            w = new Worker("/static/js/clients/s_worker.js");
        }
        w.postMessage(json);
        w.onmessage = function (ev) {
            for (let i = 0; i < parent_curr_state.length; i++) {
                characters[i].setAttribute('state_time', ev.data['state_change_time']);

                if (getFullTime(ev.data['state_change_time']) > getFullTime(ev.data['prev_state_time'])) {
                    characters[i].innerHTML = 'x';
                    characters[i].style.display = 'inline-block';
                } else {
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

                } else if (id == 11) {
                    if (getFullTime(ev.data['action_time']) == '-' || getFullTime(ev.data['action_time']) == 'ISO.undefined.0 0' || getFullTime(ev.data['action_time']) == '0.undefined.0 0') {
                        parent_curr_state[i].innerHTML = "";
                        parent_curr_state[i].style.backgroundColor = 'transparent';
                    } else if (ev.data['action_taken'] == "YES") {
                        parent_curr_state[i].innerHTML = getFullTime(ev.data['action_time']);
                        parent_curr_state[i].style.backgroundColor = '#002aaa';
                        parent_curr_state[i].style.color = 'white';
                    }

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
                'bg_Color': '#002aaa',
                'state': 'Закрыто'
            }
        }
        if (state == "OFF") {
            return {
                'bg_Color': 'red',
                'state': 'Открыто'
            }
        }
        if (state == "-") {
            return {
                'bg_Color': 'transparent',
                'state': ''
            }
        }
    }else if (id == 5){  // suv datchik
        if (state == "ON") {
            return {
                'bg_Color': 'red',
                'state': 'Вода капала'
            }
        }
        if (state == "OFF") {
            return {
                'bg_Color': '#002aaa',
                'state': 'Сухой'
            }
        }
        if (state == "-") {
            return {
                'bg_Color': 'transparent',
                'state': ''
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
                'bg_Color': '#002aaa',
                'state': 'Внешнее питание'
            }
        }
        if (state == "-") {
            return {
                'bg_Color': 'transparent',
                'state': ''
            }
        }
    }  else if (id == 7){  // pajarni datchik
        if (state == "ON") {
            return {
                'bg_Color': 'red',
                'state': 'Обнаружен дым'
            }
        }
        if (state == "OFF") {
            return {
                'bg_Color': '#002aaa',
                'state': 'Дым не обнаружен'
            }
        }
        if (state == "-") {
            return {
                'bg_Color': 'transparent',
                'state': ''
            }
        }
    } else  {
        if (state == "ON") {
            return {
                'bg_Color': '#002aaa',
                'state': 'Включен'
            }
        }
        if (state == "OFF") {
            return {
                'bg_Color': 'red',
                'state': 'Выключен'
            }
        }
        if (state == "-") {
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

//get my products open
function myProducts() {
    window.open('/clients/my_products', '_self');
}
//get my products close

function changeInput1() {
    var fistDate1 = document.getElementById('start_date').value;

    document.getElementById('end_date').value = fistDate1;
}

function changeInput2() {

    var secondDate = document.getElementById('start_date1').value;

    document.getElementById('end_date1').value = secondDate;
}

//flower open
let flower_pot_time0 = document.getElementById('flower_pot_time0');
let flower_pot_time1 = document.getElementById('flower_pot_time1');
let flower_pot_time2 = document.getElementById('flower_pot_time2');

window.addEventListener('load', function () {
    let ser_num_tuvak = socket_img[0].getAttribute('ser_num');
    let prefix_tuvak = socket_img[0].getAttribute('prefix');
    let w1;
    let json = {
        'ser_num': ser_num_tuvak,
        'prefix': prefix_tuvak
    };

    if (typeof (Worker) !== "undefined") {
        if (typeof (w1) == "undefined") {
            w1 = new Worker("/static/js/clients/tuvak_worker.js");
        }
        w1.postMessage(json)

        w1.onmessage = function (ev) {
            if (ev.data['temp'] == "-" && ev.data['soil_moist'] == "-" && ev.data['air_humid'] == "-") {
                flower_pot_time0.innerHTML = "0°C";
                flower_pot_time1.innerHTML = "0%";
                flower_pot_time2.innerHTML = "0%";
            } else {
                flower_pot_time0.innerHTML = ev.data['temp'] + "°C";
                flower_pot_time1.innerHTML = ev.data['soil_moist'] + "%";
                flower_pot_time2.innerHTML = ev.data['air_humid'] + "%";
            }
        };
    }

});
//flower close

// gaz open
let gaz_pot_time = document.getElementById('gaz_pot_time');
window.addEventListener('load', function () {
    let ser_num_tuvak = socket_img[0].getAttribute('ser_num');
    let prefix_tuvak = socket_img[0].getAttribute('prefix');

    let w1;
    let json = {
        'ser_num': ser_num_tuvak,
        'prefix': prefix_tuvak
    };

    if (typeof (Worker) !== "undefined") {
        if (typeof (w1) == "undefined") {
            w1 = new Worker("/static/js/clients/gaz_worker.js");
        }
        w1.postMessage(json)

        w1.onmessage = function (ev) {
            if (ev.data['gas_value'] == "-") {
                gaz_pot_time.innerHTML = "0";
            } else {
                gaz_pot_time.innerHTML = ev.data['gas_value'];

            }
        };
    }
});
// gaz close

//waterMeasurement function open
if (id == 11) {

    function waterMeasurement() {
        const water_measurement = document.getElementById('water_measurement');
        const prefix = water_measurement.getAttribute('prefix');
        const ser_num = water_measurement.getAttribute('ser_num');
        const start_date1 = document.getElementById('start_date1').value;
        const end_date1 = document.getElementById('end_date1').value;

        const json = {
            'prefix': prefix,
            'start_date': start_date1 + 'T00:00',
            'end_date': end_date1 + 'T23:59'
        };

        xhttp.open("Post", "/clients/my_products/my_product/get_measurements/" + ser_num);
        xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
        xhttp.send(JSON.stringify(json));

        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                let resp = JSON.parse(this.responseText);

                if (!resp['data']['serial_num']) {
                    tbody_date1.innerHTML = '';
                } else {
                    for (let i = resp['data']['serial_num'].length - 1; i >= 0; i--) {
                        let tr = document.createElement('TR');
                        tr.setAttribute('id', 'tbody_tr');

                        let td1 = document.createElement('TD');
                        let td2 = document.createElement('TD');
                        let td3 = document.createElement('TD');
                        let td4 = document.createElement('TD');

                        td1.setAttribute('class', 'state_time_on_of');
                        td2.setAttribute('class', 'state_time_on_of');
                        td3.setAttribute('class', 'state_time_on_of');
                        td4.setAttribute('class', 'state_time_on_of');

                        td1.innerHTML = resp['data']['temp'][i] + "°C";
                        td2.innerHTML = resp['data']['soil_moist'][i] + "%";
                        td3.innerHTML = resp['data']['air_humid'][i] + "%";
                        td4.innerHTML = getFullTime(resp['data']['measured_time'][i]);

                        tr.appendChild(td1);
                        tr.appendChild(td2);
                        tr.appendChild(td3);
                        tr.appendChild(td4);

                        tbody_date1.appendChild(tr);
                    }
                }

            }
        }

    }

    document.getElementById('data_form1').addEventListener('submit', function (event) {
        event.preventDefault();

        waterMeasurement();
        openFlower();
    })
}
//waterMeasurement function close

if (id == 3) {
// gazMeasurement function open
    const overlayGaz = document.querySelector('.overlay5');
    const modalGaz = document.querySelector('.modal5');
    const btnCloseModalGaz = document.querySelector('.close-modal-gaz');

    function openModalGaz1() {
        modalGaz.classList.remove('hidden5');
        overlayGaz.classList.remove('hidden5');
    };

    const closeModalGaz = function () {
        modalGaz.classList.add('hidden5');
        overlayGaz.classList.add('hidden5');
        location.reload();
    };

    btnCloseModalGaz.addEventListener('click', closeModalGaz);


    function gazDec() {

        let gaz_measurement = document.getElementById('gaz_measurement');
        let prefix = gaz_measurement.getAttribute('prefix');
        let ser_num = gaz_measurement.getAttribute('ser_num');
        let start_date1 = document.getElementById('start_date_gaz').value;
        let end_date1 = document.getElementById('end_date_gaz').value;

        let json = {
            'prefix': prefix,
            'start_date': start_date1 + 'T00:00',
            'end_date': end_date1 + 'T23:59'
        }

        xhttp.open("Post", "/clients/my_products/my_product/get_gas_values/" + ser_num);
        xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
        xhttp.send(JSON.stringify(json));

        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                let resp = JSON.parse(this.responseText);
                if (!resp['data']['serial_num']) {
                    tbody_date1.innerHTML = '';

                } else {
                    for (let i = resp['data']['log_id'].length - 1; i >= 0; i--) {
                        let tr = document.createElement('TR');
                        tr.setAttribute('id', 'tbody_tr');

                        let td1 = document.createElement('TD');
                        let td2 = document.createElement('TD');

                        td1.setAttribute('class', 'state_time_on_of');
                        td2.setAttribute('class', 'state_time_on_of');

                        td1.innerHTML = resp['data']['gas_value'][i];
                        td2.innerHTML = getFullTime(resp['data']['gas_value_time'][i]);

                        tr.appendChild(td1);
                        tr.appendChild(td2);

                        tbody_date2.appendChild(tr);
                    }
                }

            }
        }


    }


    document.getElementById('data_form_gaz').addEventListener('submit', function (event) {
        event.preventDefault();

        gazDec();
        openModalGaz1();
    })

    function changeInputGaz() {

        var secondDate = document.getElementById('start_date_gaz').value;

        document.getElementById('end_date_gaz').value = secondDate;
    }

// gazMeasurement function close

}
