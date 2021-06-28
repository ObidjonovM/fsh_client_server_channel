


function deleteType() {
    const emp_id = document.getElementById("emp_id")
    let xhttp = new XMLHttpRequest();
    xhttp.open('DELETE', '/employees/delete_type/' + emp_id.value, true)
    xhttp.send()

    xhttp.onreadystatechange = () => {
       if (this.readyState == 4 && this.status == 200) {
           console.log(this.responseText);
       }
    }
} 
