const subs_id = document.getElementById("subs_id");

function deleteSubs() {

    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result){

        xhttp.open('DELETE', '/clients/subscription/delete/' + subs_id.value, true);

        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");

        xhttp.send();

        xhttp.onreadystatechange = () => {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/clients/subscription/all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }
            }
        }

    }

}



function updateSubs() {
    window.open('/clients/subscription/update/' + subs_id.value, '_self');
}


function otmenFunction () {
    window.open('/clients/subscription/all', '_self');
}
