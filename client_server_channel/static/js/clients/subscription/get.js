function deleteSubs() {
    const subs_id = document.getElementById("subs_id")
    let xhttp = new XMLHttpRequest();
    xhttp.open('DELETE', '/clients/subscription/delete/' + subs_id.value, true)
    xhttp.send()

    xhttp.onreadystatechange = () => {
       if (this.readyState == 4 && this.status == 200) {
	   console.log(this.responseText);
       } 
    }

}