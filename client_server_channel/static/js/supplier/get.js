const supplier_id = document.getElementById("supplier_id");

function deleteSupp() {

    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result) {

        xhttp.open('DELETE', '/supplier/delete/' + supplier_id.value, true);

        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");

        xhttp.send();

        xhttp.onreadystatechange = () => {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/supplier/all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }
            }
        }

    }
}


function updateSupp() {
    window.open('/supplier/update/' + supplier_id.value, '_self');
}


function otmenFunction () {
    window.open('/supplier/all', '_self');
}
