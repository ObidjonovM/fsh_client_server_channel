function Logout() {
    window.open('/clients/logout', '_self');
}

// modal open
'use strict';

const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.close-modal');
const btnCloseModal2 = document.querySelector('.close-modal2');
const btnOpenModal = document.querySelector('.show-modal');

const openModal = function () {
    modal.classList.remove('hidden');
    overlay.classList.remove('hidden');
};

const closeModal = function () {
    modal.classList.add('hidden');
    overlay.classList.add('hidden');
};

const closeModal2 = function () {
    modal.classList.add('hidden');
    overlay.classList.add('hidden');
};
// for (let i = 0; i < btnsOpenModal.length; i++)
btnOpenModal.addEventListener('click', openModal);

btnCloseModal.addEventListener('click', closeModal);
btnCloseModal2.addEventListener('click', closeModal2);
// overlay.addEventListener('click', closeModal);

document.addEventListener('keydown', function (e) {
    // console.log(e.key);

    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
        closeModal();
    }
});
// modal close


function productImg() {
    const imgs = document.getElementsByTagName('img');

    for (let i=0; i<imgs.length; i++){
       var x = imgs[i].getAttribute("ser_num");
        console.log(x);
        // window.open('/clients/my_products/'+ x, '_self');
    }
}