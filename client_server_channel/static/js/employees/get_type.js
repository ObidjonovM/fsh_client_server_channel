const emp_id = document.getElementById("emp_id");

function deleteType() {
    let xhttp = new XMLHttpRequest();
    var result = confirm("Удалить ?");

    if (result){
        xhttp.open('DELETE', '/employees/delete_type/' + emp_id.value, true);
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
}


function updateType() {
    window.open('/employees/update_type/' + emp_id.value, '_self');
}



function otmenFunction () {
    window.open('/employees/get_types', '_self');
}
