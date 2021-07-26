const sp_id = document.getElementById("sp_id");

function deleteSpWarehouse() {
    let xhttp = new XMLHttpRequest();
    var result = confirm("Удалить ?");

    if (result){
        xhttp.open('DELETE', '/sp_warehouse/delete/' + sp_id.value, true);
        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
        xhttp.send();
        xhttp.onreadystatechange = () => {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                
            }
        }
    }
}