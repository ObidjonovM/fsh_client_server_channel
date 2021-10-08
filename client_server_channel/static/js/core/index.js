
window.onload = function () {
    localStorage.removeItem('openModal');
}
//local storage new page modal open
function addProduct() {
    window.open('/clients/my_products', '_self');
    if (typeof(Storage) !== "undefined") {
        localStorage.setItem("openModal", "open");
    }
}
//local storage new page modal close

// sign in open model
function SignIn() {
    window.open('/clients/login', '_self');
}
// sign in close model

// client logout open
function Logout() {
    window.open('/clients/logout', '_self');
}
// client logout close

// account id open
function Account() {
    window.open('/clients/account', '_self');
}
// account id close


//products id open
function Products() {
    window.open('/clients/my_products', '_self');
}
//products id close

//img onclick open
function getInfo(ev) {
    let x = ev.getAttribute("id");
    window.open('/products/info/' + x, '_self');
}
//img onclick close


//get info two open
function getInfoTwo(ev){
    let x = ev.previousElementSibling.getAttribute("id");
    window.open('/products/info/' + x, '_self');
}
//get info two close