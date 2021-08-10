window.addEventListener("load", function () {
    function sendData() {
        const XHR = new XMLHttpRequest();

        const FD = new FormData(form);

        XHR.addEventListener("load", function (event) {

            if (event.target.responseURL == window.location.href) {
                const resp = JSON.parse(event.target.responseText);
                if (resp.log_code == -1) {
                    alert('Данная должность уже сушествует');
                }
            } else {
                location.href = event.target.responseURL;
            }
        });

        XHR.addEventListener("error", function (event) {
            alert('Error');
        });

        XHR.open("POST", "/sp_logistic/add");

        XHR.send(FD);
    }

    const form = document.getElementById("myForm");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        sendData();
    });
});


function otmenFunction() {
    window.open('/sp_logistic/all', '_self');
}


function getTrStatusByCarrId() {
    let tr_status_id = document.getElementById('tr_status_id');
    let tr_status_option = tr_status_id.getElementsByTagName('option');
    let carrier_id = document.getElementById('carrier_id');
    let default_status = document.getElementById('default_status');

    for (let i = 1; i < tr_status_option.length; i++) {
        if (carrier_id.value == tr_status_option[i].getAttribute('carrier_id')) {
            tr_status_option[i].style.display = 'block';
            default_status.removeAttribute('selected');
            default_status.setAttribute('selected', 'selected');
        }
        else {
            tr_status_option[i].style.display = 'none';
            default_status.removeAttribute('selected');
            default_status.setAttribute('selected', 'selected');
        }
    }
}