const fw_id = document.getElementById("fw_id");

function deleteFirm() {
    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result) {
        xhttp.open('DELETE', '/products/firmware/delete/' + fw_id.value, true);

        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");

        xhttp.send();

        xhttp.onreadystatechange = () => {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/products/firmware/all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }
            }

        }

    }

}


function updateFirm() {
    window.open('/products/firmware/update/' + fw_id.value, '_self');
}

function otmenFunction() {
    window.open('/products/firmware/all', '_self');
}
