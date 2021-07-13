function deleteDealer() {
    const dealer_id = document.getElementById("dealer_id")
    let xhttp = new XMLHttpRequest();
    xhttp.open('DELETE', '/products/dealer/delete/' + dealer_id.value, true)
    xhttp.send()

    xhttp.onreadystatechange = () => {
       if (this.readyState == 4 && this.status == 200) {
	   console.log(this.responseText);
       } 
    }

}