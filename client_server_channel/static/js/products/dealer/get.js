const dealer_id = document.getElementById("dealer_id");

function deleteDealer() {

    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result){

        xhttp.open('DELETE', '/products/dealer/delete/' + dealer_id.value, true);

        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");

        xhttp.send();

        xhttp.onreadystatechange = () => {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/products/dealer/all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }
            }
        }

    }

}


function updateType() {
    window.open('/products/dealer/update/' + dealer_id.value, '_self');
}


function otmenFunction () {
    window.open('/products/dealer/all', '_self');
}
