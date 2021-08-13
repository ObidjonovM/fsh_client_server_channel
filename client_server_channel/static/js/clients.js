// header dagi hi-person clasi uchun ochildi
const account_products = document.getElementById('account-products');
const container = document.getElementById('container');

function displayBlock() {
    account_products.style.display = "block";
    container.style.backgroundColor = "rgba(0,0,0,.3)";
    container.style.transition = "all .4s ease"
}

function displayNone() {
    account_products.style.display = "none";
    container.style.backgroundColor = "#fff";
    container.style.transition = "all .4s ease"
}

function accountProductsBlock() {
    account_products.style.display = "block";
    container.style.backgroundColor = "rgba(0,0,0,.3)";
    container.style.transition = "all .4s ease"
}

function accountProductsNone() {
    account_products.style.display = "none";
    container.style.backgroundColor = "#fff";
    container.style.transition = "all .4s ease"
}
// header dagi hi-person clasi uchun yopildi




// header dagi account-products clasi uchun ochildi
const account = document.getElementById('account');

account.addEventListener('click', () => {
    window.open('/clients/update', '_self');
})
// header dagi account-products clasi uchun yopildi







const modal_products = document.getElementById('modal-products');
const products = document.getElementById('products');
const close = document.getElementById('close');
const closeBtn = document.getElementById('closeBtn');

products.addEventListener('click', () => {
    document.getElementById('modal-products').style.display = "block";
})

close.addEventListener('click', () => {
    document.getElementById('modal-products').style.display = "none";

})

closeBtn.addEventListener('click', () => {
    document.getElementById('modal-products').style.display = "none";

})

// modal_products.addEventListener('click', () => {
//     document.getElementById('modal-products').style.display = "none";
//
// })