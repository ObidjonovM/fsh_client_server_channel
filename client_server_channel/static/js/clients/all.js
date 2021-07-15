function deleteClient(e) {
    let client_id = e.parentNode.parentNode.children[0].innerHTML;

    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result){

        xhttp.open('DELETE', '/clients/delete/' + client_id, true);

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
    else {
        return false;
    }

}

document.getElementById("addClick").onclick = () => {
    window.open('/clients/add', '_self');
};

function getClient(e) {
    window.open('/clients/get/' + e.children[0].innerHTML, '_self');
}

