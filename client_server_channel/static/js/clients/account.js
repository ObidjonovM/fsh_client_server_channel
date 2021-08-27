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
    document.getElementById('modal-products').style.display = "block";
})

close.addEventListener('click', () => {
    document.getElementById('modal-products').style.display = "none";

})

closeBtn.addEventListener('click', () => {
    document.getElementById('modal-products').style.display = "none";

})