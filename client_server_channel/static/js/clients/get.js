const client_id = document.getElementById("client_id");

function deleteClient() {

    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result){

        xhttp.open('DELETE', '/clients/delete/' + client_id.value, true);

        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");

        xhttp.send();

        xhttp.onreadystatechange = () => {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/clients/all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }
            }

        }

    }

}

function updateClient() {
    window.open('/clients/update/' + client_id.value, '_self');
}

function otmenFunction (){
    window.open('/clients/all', '_self');
}
