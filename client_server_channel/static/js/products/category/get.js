const cat_id = document.getElementById("cat_id");

function deleteCat() {
    let xhttp = new XMLHttpRequest();
    var result = confirm("Удалить ?");

    if (result){
        xhttp.open('DELETE', '/products/category/delete/' + cat_id.value, true);
        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
        xhttp.send();
        xhttp.onreadystatechange = () => {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/products/category/all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }
            }
        }
    }
}


function updateType() {
    window.open('/products/category/update/' + cat_id.value, '_self');
}


function otmenFunction () {
    window.open('/products/category/all', '_self');
}
