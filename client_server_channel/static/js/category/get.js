function deleteCat() {
    const cat_id = document.getElementById("cat_id")
    let xhttp = new XMLHttpRequest();
    xhttp.open('DELETE', '/products/category/delete/' + cat_id.value, true)
    xhttp.send()

    xhttp.onreadystatechange = () => {
       if (this.readyState == 4 && this.status == 200) {
	   console.log(this.responseText);
       } 
    }

}