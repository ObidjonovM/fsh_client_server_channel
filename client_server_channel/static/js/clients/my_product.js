

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

    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
        closeModal();
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
// const xhttp = new XMLHttpRequest();

let url = window.location.href;
function OpenNewModal() {
    xhttp.open('POST', '/clients/my_products/my_product/info/' + url.substring(url.lastIndexOf('/') + 1), true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send(JSON.stringify({'password' : forInfoPass.value}));
    console.log(forInfoPass.value)
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let resp = JSON.parse(this.responseText);
            if (resp['data']['ap_password']) {
                containerModal.innerHTML = "<button class=\"close-modal3\" onclick=\"closeModal3()\">&times;</button>\n" +
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


document.addEventListener('keydown', function (e){
    if (e.key === 'Enter'){
        OpenNewModal();
    }
})


let informationOnOf1 = document.querySelector('.informationOnOf1');
 function informationOnOf(e){
     let json = {
         'ser_num' : e.getAttribute('ser_num'),
         'prefix' : e.getAttribute('prefix')
     }

     console.log(json);
     xhttp.open('Post', '/clients/my_products/my_product/last_request_time');
     xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
     xhttp.send(JSON.stringify(json))
     xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
             let resp = JSON.parse(this.responseText);
                let div = document.createElement('DIV');
                console.log(resp['request_time']);
               informationOnOf1.innerHTML = "<h2 style='border: 1px solid #6c6b6b'>" +resp['request_time']+ "</h2>\n"
         }
     }
 }





const socket_img = document.querySelectorAll('.socket-img');
const  req_action = document.getElementsByClassName('ONOF');
window.addEventListener('load', function (){

    let w;
    let serNums = [];
    let prefixes = [];
    for (let i=0; i < socket_img.length; i++) {
        serNums.push(socket_img[i].getAttribute('ser_num'));
        prefixes.push(socket_img[i].getAttribute('prefix'));
    }
    let json = {
        'ser_nums': serNums,
        'prefixs': prefixes
    }
    if (typeof(Worker) !== "undefined") {
        if (typeof (w) == "undefined") {
            w = new Worker("/static/js/clients/s_worker.js");
        }
        w.postMessage(json)
        w.onmessage = function (ev) {
            for (let i=0; i < socket_img.length; i++) {
                for (let j in ev.data['data']) {
                    var key = j;
                    var val = ev.data['data'][j];
                    for (var a in val) {
                        var sub_key = a;
                        var sub_val = val[a];
                        if (socket_img[i].getAttribute('ser_num') == sub_key) {
                            socket_img[i].setAttribute('action', sub_val['state']);
                            req_action[i].innerHTML = sub_val['state'];
                            // console.log(sub_val['state'])
                        }
                    }
                }
            }
        };
    }

})
