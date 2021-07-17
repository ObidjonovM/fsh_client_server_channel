function deleteType() {
    const fw_id = document.getElementById("fw_id")
    console.log(fw_id)
    let xhttp = new XMLHttpRequest();
    xhttp.open('DELETE', '/products/firmware/delete/' + fw_id.value, true)
    xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
    xhttp.send()
const fw_id = document.getElementById("fw_id");

function deleteFirm() {
    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result) {
        xhttp.open('DELETE', '/firmwares/delete/' + fw_id.value, true);

        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");

        xhttp.send();

        xhttp.onreadystatechange = () => {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/firmwares/get_all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }
            }

        }

    }

}


function updateFirm() {
    window.open('/firmwares/update/' + fw_id.value, '_self');
}

function otmenFunction() {
    window.open('/firmwares/get_all', '_self');
}
