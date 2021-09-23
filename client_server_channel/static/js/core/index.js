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

function addProduct() {
    window.open('/clients/my_products', '_self');
}

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


function getInfo(ev) {
    let x = ev.getAttribute("id");
    window.open('/products/info/' + x, '_self');
}