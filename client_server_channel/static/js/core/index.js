// sign in open model

function SignIn() {
    window.open('/clients/login', '_self');
}

// sign in close model




// Acardion js and image open


const product_img = document.getElementById('product_img')
var xhttp = new XMLHttpRequest();

function get_sub_cat(e) {
    let cat_id = {'cat_id': e.id}
    xhttp.open('POST', '/', true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send(JSON.stringify(cat_id));
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let resp = JSON.parse(this.responseText);
            if (resp['data']['category_id'] != undefined) {
                if (e.nextSibling == null || e.nextElementSibling == null) {
                    let ul = document.createElement('UL');
                    ul.setAttribute('class', 'submenu');

                    for (let i = 0; i < resp['data']['category_id'].length; i++) {
                        var li = document.createElement('LI');
                        let a = document.createElement('A');
                        a.setAttribute('onmousedown', 'get_sub_cat(this)');
                        a.setAttribute('onmouseup', 'open_sub_cat(this)');
                        a.setAttribute('class', 'link');
                        a.setAttribute('id', resp['data']['category_id'][i]);
                        let textnode = document.createTextNode(resp['data']['name'][i]);
                        a.appendChild(textnode);
                        li.appendChild(a);
                        ul.appendChild(li);
                    }
                    e.parentNode.appendChild(ul);
                }
            } else {

                xhttp.open('POST', '/products/info/' + e.id, true)
                xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
                xhttp.send();
                xhttp.onreadystatechange = function () {
                    if (this.readyState == 4 && this.status == 200) {
                        product_img.innerHTML = '';
                        let resp = JSON.parse(this.responseText);
                        if (resp['data']['product_id'] != undefined) {
                            for (let j = 0; j < resp['data']['product_id'].length; j++) {
                                let div = document.createElement('DIV');
                                let img = document.createElement('img');
                                img.setAttribute('id', resp['data']['product_id'][j]);
                                img.setAttribute('src', resp['data']['photo'][j]);
                                img.setAttribute('width', '20%');
                                div.appendChild(img);
                                product_img.appendChild(div);
                            }
                        }
                    }
                }
            }
        }
    }



}









function open_sub_cat(e) {
    if (e.nextElementSibling.style.display === 'block'){
        e.style.color = '#4D4D4D';
        e.nextElementSibling.style.display = 'none';
        e.nextElementSibling.style.transaction = '.9s ease';

    }else {
        e.nextElementSibling.style.display = 'block';
        e.nextElementSibling.style.transaction = '.9s ease';
        e.style.color = 'black';
    }
    e.classList.toggle('active');

    // if (e.nextElementSibling){
    //      let i = e.nextElementSibling.children.document.createElement('I');
    //     i.setAttribute('class', 'fa fa-chevron-down');
    // }
}

// Acardion and image js close



/***** modal open  *****/

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

/***** modal close  *****/