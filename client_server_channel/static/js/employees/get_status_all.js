// Delete ni bosganda rostan ham o'chirilsinmi deb so'rash logikasi ha desa true yo'q desa false
function deleteStatus(e) {
    let status_id = e.parentNode.parentNode.children[0].innerHTML;
    let xhttp = new XMLHttpRequest();
    var result = confirm("Удалить ?");

    if (result) {
        xhttp.open('DELETE', '/employees/delete_status/' + status_id, true);
        xhttp.setRequestHeader("Content-type", "application/json;charset=UTF-8");
        xhttp.send();
        xhttp.onreadystatechange = () => {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
                const resp = JSON.parse(xhttp.responseText);
                if (resp['success']) {
                    window.open('/employees/get_status_all', '_self')
                } else {
                    alert('Не удалось удалить тип сотрудника!');
                }
            }
        };
        return true;
    }
    return false;
}

// dobavit uchun js code
document.getElementById("addClick").onclick = function () {
    location.href = "http://127.0.0.1:5000/employees/add_status";
};

// get_types dagi malumotlarni get_type ga olib boradi tr ni ikki marta click qilganda
function getType(e) {
    location.href = "http://127.0.0.1:5000/employees/get_status/" + e.children[0].innerHTML;
}
