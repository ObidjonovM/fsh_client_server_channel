function deleteProduct() {
    const product_id = document.getElementById("product_id")
    let xhttp = new XMLHttpRequest();
    xhttp.open('DELETE', '/products/info/delete/' + product_id.value, true)
    xhttp.send()

    xhttp.onreadystatechange = () => {
       if (this.readyState == 4 && this.status == 200) {
	   console.log(this.responseText);
       } 
    }

}