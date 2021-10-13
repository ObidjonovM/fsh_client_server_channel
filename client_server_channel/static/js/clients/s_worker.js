var xhttp = new XMLHttpRequest();
let json = {}
self.addEventListener("message", function(e) {
    json = e.data
}, false);


function timedCount() {

    if (!json['ser_nums']){

    }else {
        // console.log(json)
        xhttp.open('Post', '/clients/my_products/get_current_states', true);
        xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
        xhttp.send(JSON.stringify(json));

        xhttp.onreadystatechange = function (ev) {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                postMessage(resp);
            }
        }
    }
    setTimeout("timedCount()",3000);
}

timedCount();