
function deleteStatus() {
const status_id = document.getElementById("status_id");

    let xhttp = new XMLHttpRequest();
    var result = confirm("Удалить ?");

    if (result){
        xhttp.open('DELETE', '/employees/status/delete/' + status_id.value, true);
        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
        xhttp.send();
        xhttp.onreadystatechange = () => {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/employees/status/all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }
            }
        }
    }
}


function updateStatus() {
    window.open('/employees/status/update/' + status_id.value, '_self');
}



function otmenFunction (){
    window.open('/employees/status/all', '_self');
}
