const detail_id = document.getElementById("detail_id");

function deleteSpOrderDetail() {

    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result){

        xhttp.open('DELETE', '/sp_order_detail/delete/' + detail_id.value, true);

        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");

        xhttp.send();

        xhttp.onreadystatechange = () => {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/sp_order_detail/all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }
            }

        }

    }

}

function otmenFunction (){
    window.open('/sp_order_detail/all', '_self');
}
