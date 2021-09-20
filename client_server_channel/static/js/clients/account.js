// account id open
const account = document.getElementById('account');

account.addEventListener('click', () => {
    window.open('/clients/update', '_self');
})
// account id close


const products = document.getElementById('products');
const close = document.getElementById('close');
const closeBtn = document.getElementById('closeBtn');

products.addEventListener('click', () => {
    window.open('/clients/my_products', '_self');
})

close.addEventListener('click', () => {
    document.getElementById('modal-products').style.display = "none";

})

closeBtn.addEventListener('click', () => {
    document.getElementById('modal-products').style.display = "none";

})

function Logout() {
    window.open('/clients/logout', '_self');
}