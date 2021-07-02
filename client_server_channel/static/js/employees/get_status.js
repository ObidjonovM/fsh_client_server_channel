


function deleteType() {
    const status_id = document.getElementById("status_id")
    let xhttp = new XMLHttpRequest();
    xhttp.open('DELETE', '/employees/delete_status/' + status_id.value, true)
    xhttp.send()

    xhttp.onreadystatechange = () => {
       if (this.readyState == 4 && this.status == 200) {
           console.log(this.responseText);
       }
    }
} 
