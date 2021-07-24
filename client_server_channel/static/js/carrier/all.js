// Delete ni bosganda rostan ham o'chirilsinmi deb so'rash logikasi ha desa true yo'q desa false: ?
function deleteCurr(e) {
    let carrier_id = e.parentNode.parentNode.children[0].innerHTML;

    let xhttp = new XMLHttpRequest();

    var result = confirm("Удалить ?");

    if (result) {

        xhttp.open('DELETE', '/carrier/delete/' + carrier_id, true);

        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");

        xhttp.send();

        xhttp.onreadystatechange = () => {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);

                if (resp['success']) {
                    window.open('/carrier/all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }

            }

        };
        return true;
    }
    return false;
}

// dobavit uchun js code: Ishlayapti
document.getElementById("addClick").onclick = function () {
    window.open('/carrier/add', '_self');
};

// get_types dagi malumotlarni get_type ga olib boradi tr ni ikki marta click qilganda: ?
function getType(e) {
    window.open('/carrier/get/' + e.children[0].innerHTML, '_self');
}
