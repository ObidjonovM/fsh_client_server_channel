

function deleteType(e) {
    let emp_type_id = e.parentNode.parentNode.children[0].innerHTML;
    let xhttp = new XMLHttpRequest();
    var result = confirm("Удалить ?");

    if (result){
        xhttp.open('DELETE', '/employees/delete_type/' + emp_type_id, true);
        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
        xhttp.send();
        xhttp.onreadystatechange = () => {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/employees/get_types', '_self')
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
    window.open('/employees/add_type', '_self');
};

function getType(e) {
    window.open('/employees/get_type/' + e.children[0].innerHTML, '_self');
}

