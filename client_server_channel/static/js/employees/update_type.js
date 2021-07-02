function otmenFunction(){
    var url = window.location.href;
    var value = url.substr(url.lastIndexOf('/')+1);
    console.log(value);
    location.href = "http://127.0.0.1:5000/employees/get_type/"+ value;
}


