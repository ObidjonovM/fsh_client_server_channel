var xhttp = new XMLHttpRequest();
let json = {}
self.addEventListener("message", function(e) {
    json = e.data
}, false);


function timedCount() {

    if (!json['ser_num']){

    }else {
        xhttp.open('Post', '/clients/my_products/my_product/get_current_state', true);
        xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
        xhttp.send(JSON.stringify(json));

        xhttp.onreadystatechange = function (ev) {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp1 = JSON.parse(xhttp.responseText);
               try {
                   postMessage(resp1);
               }
               catch (e) {
                   console.log("Error: ", e);
                   if (e.name == 'InvalidStateError') {
                       window.location.reload();
                   }
               }

            }
        }
    }
    setTimeout("timedCount()",1000);
}

timedCount();
