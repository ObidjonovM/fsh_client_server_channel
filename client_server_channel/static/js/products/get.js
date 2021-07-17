const product_id = document.getElementById("product_id");

function deleteProduct() {

    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result){

        xhttp.open('DELETE', '/products/delete/' + product_id.value, true);

        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");

        xhttp.send();

        xhttp.onreadystatechange = () => {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                
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
