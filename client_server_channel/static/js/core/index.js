window.onload = function () {
    localStorage.removeItem('openModal');
};
//local storage new page modal open
function addProduct() {
    window.open('/clients/my_products', '_self');
    if (typeof(Storage) !== "undefined") {
        localStorage.setItem("openModal", "open");
    }
}
//local storage new page modal close

//img onclick open
function getInfo(ev) {
    let x = ev.getAttribute("id");
    window.open('/products/info/' + x, '_self');
}
//img onclick close

// let aaaa = document.querySelector('img-div');
function openProductInfo(ev) {
    let firs_child = ev.firstChild;
    let span = firs_child.nextElementSibling;
    let img_id = span.nextElementSibling.getAttribute('id');
    window.open('/products/info/' + img_id, '_self');
}