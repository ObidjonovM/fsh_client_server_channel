// sign in open model

function SignIn() {
    window.open('/clients/login', '_self');
}

// sign in close model


// Acardion js and image open
const link = document.querySelectorAll('.link');
const submenu = document.querySelectorAll('.submenu');
const icon = document.querySelectorAll('.fa-chevron-down');
for (let i = 0; i < link.length; i++) {

    link[i].onclick = function () {
        submenu[i].classList.toggle('active');
        icon[i].classList.toggle('active');
    }

}


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
                    for (let i = 0; i < resp['data']['category_id'].length; i++) {
                        var li = document.createElement('LI');
                        let a = document.createElement('A');
                        a.setAttribute('onclick', 'get_sub_cat(this)');
                        a.setAttribute('id', resp['data']['category_id'][i]);
                        let textnode = document.createTextNode(resp['data']['name'][i]);
                        a.appendChild(textnode);
                        li.appendChild(a);
                        ul.appendChild(li);
                    }
                    e.parentNode.appendChild(ul)
                }
            } else {
                xhttp.open('POST', '/products/info/' + e.id, true)
                xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
                xhttp.send();
                xhttp.onreadystatechange = function () {
                    if (this.readyState == 4 && this.status == 200) {
                        product_img.innerHTML = ''
                        let resp = JSON.parse(this.responseText);
                        if (resp['data']['product_id'] != undefined) {
                            for (let j = 0; j < resp['data']['product_id'].length; j++) {
                                let img = document.createElement('img');
                                img.setAttribute('id', resp['data']['product_id'][j]);
                                img.setAttribute('src', resp['data']['photo'][j]);
                                img.setAttribute('width', '20%');
                                product_img.appendChild(img)
                            }
                        }
                    }
                }
            }
        }
    }
}

// Acardion and image js close