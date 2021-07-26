const shipping_type_id = document.getElementById("shipping_type_id");

function deleteShippType() {

    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result) {

        xhttp.open('DELETE', '/shipping_type/delete/' + shipping_type_id.value, true);

        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");

        xhttp.send();

        xhttp.onreadystatechange = () => {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/shipping_type/all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }
            }
        }

    }
}


function updateShippType() {
    window.open('/shipping_type/update/' + shipping_type_id.value, '_self');
}


function otmenFunction () {
    window.open('/shipping_type/all', '_self');
}
