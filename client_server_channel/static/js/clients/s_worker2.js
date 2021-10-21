//all time open
var xhttp = new XMLHttpRequest();
let json1 = {}
self.addEventListener("message", function(e) {
    json1 = e.data
}, false);


function timedCount() {

    if (!json1['ser_num']){

    }else {
        xhttp.open('Post', '/clients/my_products/my_product/last_request_time');
        xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
        xhttp.send(JSON.stringify(json1))
        xhttp.onreadystatechange = function (ev) {
            if (this.readyState == 4 && this.status == 200) {
                let resp = JSON.parse(this.responseText);
                postMessage(resp);
            }
        }
    }
    setTimeout("timedCount()",1000);
}

timedCount();
//all time close