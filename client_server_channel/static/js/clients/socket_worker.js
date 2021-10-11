var i = 1;
const ser_number2 = document.querySelectorAll('.s')[0].getAttribute('ser_num2');
const product_id2 = document.querySelectorAll('.s')[0].getAttribute('product_id2');
console.log(ser_number2)

// const xhttp = new XMLHttpRequest();
function timedCount() {
    i = i + 1;

    let json = {
        'ser_num': [ser_number2],
        'product_id': [product_id2]
    }

    xhttp.open('Post', '/clients/my_products/get_current_states', true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send(JSON.stringify(json));


    xhttp.onreadystatechange = function (ev) {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            // const resp = JSON.parse(xhttp.responseText);
            i = xhttp.responseText;

        }
    }
    postMessage(i);
    setTimeout("timedCount()",1000);
}

timedCount();