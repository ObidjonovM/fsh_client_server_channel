const sp_id = document.getElementById("sp_id");

function deleteSpWarehouse() {

    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result) {

        xhttp.open('DELETE', '/sp_warehouse/delete/' + sp_id.value, true);

        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");

        xhttp.send();

        xhttp.onreadystatechange = () => {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/sp_warehouse/all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }
            }
        }

    }
}


function updateSpWarehouse() {
    window.open('/sp_warehouse/update/' + sp_id.value, '_self');
}


function otmenFunction () {
    window.open('/sp_warehouse/all', '_self');
}

