function deleteType(e) {
    let serial_num = e.parentNode.parentNode.children[0].innerHTML;

    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result){

        xhttp.open('DELETE', '/products/delete/' + serial_num, true);

        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");

        xhttp.send();

        xhttp.onreadystatechange = () => {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/products/all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }
            }
        }

    }
    else {
        return false;
    }

}

document.getElementById("addClick").onclick = () => {
    window.open('/products/add', '_self');
};

function getType(e) {
    let ser_number = e.getAttribute('ser_num');
    console.log(ser_number);
    window.open('/products/get/' + ser_number, '_self');

}

const td = document.getElementsByTagName('td');
    for (let i=0; i<td.length; i++){
        if ('None'.includes(td[i].innerHTML)) {
            td[i].innerHTML = '';
        }
    }
