`// sign in open model`
const sign_in = document.getElementById('sign-in');

sign_in.addEventListener('click', () => {
    window.open('/clients/login', '_self');
})
// sign in close model


// Acardion js open

// $(function() {
//     var Accordion = function(el, multiple) {
//         this.el = el || {};
//         this.multiple = multiple || false;

//         // Variables privadas
//         var links = this.el.find('.link');
//         // Evento
//         links.on('click', {el: this.el, multiple: this.multiple}, this.dropdown)
//     }

//     Accordion.prototype.dropdown = function(e) {
//         var $el = e.data.el;
//         $this = $(this),
//             $next = $this.next();

//         $next.slideToggle();
//         $this.parent().toggleClass('open');

//         if (!e.data.multiple) {
//             $el.find('.submenu').not($next).slideUp().parent().removeClass('open');
//         };
//     }

//     var accordion = new Accordion($('#accordion'), false);
// });

// Acardion js close
const product_img = document.getElementById('product_img')
var xhttp = new XMLHttpRequest();

function get_sub_cat(e) {
    let cat_id = { 'cat_id': e.id }
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
                    }
                    ul.appendChild(li)
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
