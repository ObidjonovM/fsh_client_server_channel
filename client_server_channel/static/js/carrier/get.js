const carrier_id = document.getElementById("carrier_id");

function deleteCarr() {

    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result){

        xhttp.open('DELETE', '/carrier/delete/' + carrier_id.value, true);

        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");

        xhttp.send();

        xhttp.onreadystatechange = () => {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/carrier/all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }
            }

        }

    }

}

function updateCarr() {
    window.open('/carrier/update/' + carrier_id.value, '_self');
}

function otmenFunction (){
    window.open('/carrier/all', '_self');
}
