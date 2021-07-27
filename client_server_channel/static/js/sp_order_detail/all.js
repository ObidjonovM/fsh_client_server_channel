function deleteType(e) {
    let detail_id = e.parentNode.parentNode.children[0].innerHTML;

    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result){

        xhttp.open('DELETE', '/sp_order_detail/delete/' + detail_id, true);

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
    else {
        return false;
    }

}

document.getElementById("addClick").onclick = () => {
    window.open('/sp_order_detail/add', '_self');
};

function getType(e) {
    window.open('/sp_order_detail/get/' + e.children[0].innerHTML, '_self');
}

