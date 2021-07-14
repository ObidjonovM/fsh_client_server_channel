function deleteClient() {
    const client_id = document.getElementById('client_id')
    let xhttp = new XMLHttpRequest();
    var result = confirm("Удалить ?");

    if (result){
        xhttp.open('DELETE', '/clients/delete/' + client_id.value, true);
        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
        xhttp.send();
        xhttp.onreadystatechange = () => {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                
            }
        }
    }
}