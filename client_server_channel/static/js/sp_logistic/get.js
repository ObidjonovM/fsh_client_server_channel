const shipment_id = document.getElementById("shipment_id");

function deleteSpLogistic() {

    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result){

        xhttp.open('DELETE', '/sp_logistic/delete/' + shipment_id.value, true);

        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");

        xhttp.send();

        xhttp.onreadystatechange = () => {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/sp_logistic/all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }
            }

        }

    }

}

function updateSpLogistic() {
    window.open('/sp_logistic/update/' + shipment_id.value, '_self');
}

function otmenFunction (){
    window.open('/sp_logistic/all', '_self');
}
