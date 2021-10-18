
    var xhttp = new XMLHttpRequest();
    function actionCommand(e) {
        let action = {
            'serial_num': e.getAttribute('ser_num'),
            'action_requested': e.getAttribute('action'),
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
        xhttp.send(JSON.stringify({'password' : forInfoPass.value}));
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

    document.addEventListener('keydown', function (e){
        if (e.key === 'Enter'){
            OpenNewModal();
        }
    })


// All time open
    const containerModal2 = document.getElementById('containerModal2');
    const all_time_modal2 = document.querySelector('.modal2');
    const all_time_overlay2 = document.querySelector('.overlay2');
    const btnCloseModal2 = document.querySelector('.close-modal2');
    const all_time_input2 = document.getElementById('all_time_input');
    let informationOnOf1 = document.querySelector('.informationOnOf1');
    let information_on_of = document.querySelector('.information-on-of');


    // function closeModal4() {
    //     all_time_modal2.classList.add('hidden2');
    //     all_time_overlay2.classList.add('hidden2');
    //     all_time_input2.value = "";
    // }
    //
    // function openAllTime() {
    //     all_time_modal2.classList.remove('hidden2');
    //     all_time_overlay2.classList.remove('hidden2');
    // }

    // btnCloseModal2.addEventListener('click', closeModal4);
    // all_time_input2.addEventListener('click', openAllTime);

window.addEventListener('load', function () {


    function informationOnOf(){
         let json = {
             'ser_num' : informationOnOf1.getAttribute('ser_num'),
             'prefix' : informationOnOf1.getAttribute('prefix')
         }

        console.log(json);
         xhttp.open('Post', '/clients/my_products/my_product/last_request_time');
         xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
         xhttp.send(JSON.stringify(json))
         xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                 let resp = JSON.parse(this.responseText);

                 if (resp['request_time'] == '-'){
                     informationOnOf1.innerHTML = '';
                 }else {
                     informationOnOf1.innerHTML = resp['request_time'];
                     information_on_of.appendChild(informationOnOf1);
                 }


             }
         }
        setTimeout("informationOnOf()",1000);
     }
})
// All time close



// start_date and end_data open
    function sendData() {

        const data_form = document.getElementById('data_form');
        const ser_number = data_form.getAttribute('ser_num');
        const prefix = document.getElementById('hidden_input2');
        const start_date = document.getElementById('start_date').value;
        const end_date = document.getElementById('end_date').value;
        const tbody_date = document.getElementById('tbody_date');

        const json = {
           'prefix': prefix.getAttribute('value'),
           'start_date' : start_date,
           'end_date' : end_date
        }

        xhttp.open("Post", "/clients/my_products/my_product/logs/" + ser_number);
        xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
        xhttp.send(JSON.stringify(json));

        xhttp.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                let resp = JSON.parse(this.responseText);
                console.log(resp)
                for (let i=0; i<resp['data']['state'].length; i++){

                    let tr = document.createElement('TR');
                    tr.setAttribute('id', 'tbody_tr');

                    let td1 = document.createElement('TD');
                    let td2 = document.createElement('TD');

                    td1.setAttribute('id', 'state_time_on_of');
                    td2.setAttribute('id', 'state_time_on_of');

                    td1.innerHTML = resp['data']['state'][i];
                    td2.innerHTML = resp['data']['state_time'][i];

                    tr.appendChild(td1);
                    tr.appendChild(td2);

                    tbody_date.appendChild(tr);

                }
            }
        }
    }

    const form = document.getElementById( "data_form" );

    form.addEventListener( "submit", function ( event ) {
        event.preventDefault();

        sendData();
        open3();
    } );

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
// start_date and end_data close




//ON OF open
    const socket_img = document.querySelectorAll('.socket-img');
    const  req_action = document.getElementsByClassName('ONOF');
    window.addEventListener('load', function (){

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
        }
        if (typeof(Worker) !== "undefined") {
            if (typeof (w) == "undefined") {
                w = new Worker("/static/js/clients/s_worker.js");
            }
            w.postMessage(json)

            w.onmessage = function (ev) {
                let on_of;
                if (ev.data['state'] == 'ON'){
                    on_of = 'Включить';
                }
                if (ev.data['state'] == 'OFF'){
                    on_of = 'Выключить';
                }
                for (let i=0; i<req_action.length; i++) {
                    req_action[i].style.backgroundColor = 'white';
                    req_action[i].innerHTML = on_of;
                }
            };
        }

    })
//ON OF close