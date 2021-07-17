function deleteType() {
    const fw_id = document.getElementById("fw_id")
    console.log(fw_id)
    let xhttp = new XMLHttpRequest();
    xhttp.open('DELETE', '/products/firmware/delete/' + fw_id.value, true)
    xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
    xhttp.send()

    xhttp.onreadystatechange = () => {
       if (this.readyState == 4 && this.status == 200) {
	   console.log(this.responseText);
       } 
    }

}