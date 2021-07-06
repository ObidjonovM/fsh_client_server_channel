function deleteType() {
    const fw_id = document.getElementById("fw_id")
    let xhttp = new XMLHttpRequest();
    xhttp.open('DELETE', '/firmwares/delete/' + fw_id.value, true)
    xhttp.send()

    xhttp.onreadystatechange = () => {
       if (this.readyState == 4 && this.status == 200) {
	   console.log(this.responseText);
       } 
    }

}