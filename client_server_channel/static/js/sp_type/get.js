const sp_type_id = document.getElementById("sp_type_id");

function deleteSpType() {

    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result) {

        xhttp.open('DELETE', '/sp_type/delete/' + sp_type_id.value, true);

        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");

        xhttp.send();

        xhttp.onreadystatechange = () => {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/sp_type/all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }
            }
        }

    }
}


function updateSpType() {
    window.open('/sp_type/update/' + sp_type_id.value, '_self');
}


function otmenFunction () {
    window.open('/sp_type/all', '_self');
}

