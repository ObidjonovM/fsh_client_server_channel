const dept_id = document.getElementById("dept_id");

function deleteDept() {

    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result){

        xhttp.open('DELETE', '/employees/department/delete/' + dept_id.value, true);

        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");

        xhttp.send();

        xhttp.onreadystatechange = () => {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/employees/department/all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }
            }
        }

    }
}


function updateType() {
    window.open('/employees/department/update/' + dept_id.value, '_self');
}



function otmenFunction (){
    window.open('/employees/department/all', '_self');

}
