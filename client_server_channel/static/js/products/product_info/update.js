
const main_photo = document.getElementById('main_photo');

const div_other_photos = document.getElementById('div_other_photos');

const xhttp = new XMLHttpRequest();
let photos_id = [];
let other_photos = [];
let main_photos = [];
let product_id = [];
const url = window.location.href;
const id = url.substring(url.lastIndexOf('/')+1);

function changeMainPhoto(e) {

    let imgs = div_other_photos.querySelectorAll('img');
    e.setAttribute('main', 'True')
    for (let i = 0; i < imgs.length; i++) {
        if (imgs[i] != e) {
            imgs[i].setAttribute('main', 'False')
        }
    }
    mainPhoto()
    let result = {};
    result['photos_id'] = photos_id;
    result['main_photo'] = main_photos;
    xhttp.open('Post','/products/photo/update', true);
    xhttp.setRequestHeader("Content-type","application/json; charset=UTF-8");

    xhttp.send(JSON.stringify(result));
    xhttp.onreadystatechange = function () {
        if ((this.readyState ==4) && (this.status == 200)){
            let resp = JSON.parse(this.responseText);
            if (resp['success']) {
                main_photo.src = e.src;
            }
        }
    }
}

function mainPhoto() {
    photos_id = [];
    other_photos = [];
    main_photos = [];
    let imgs = div_other_photos.querySelectorAll('img');
    for (let i=0; i<imgs.length; i++){
        photos_id.push(imgs[i].id);
        main_photos.push(imgs[i].getAttribute('main'));
    }
}

function addForm() {
    let result = {}
    const desc = document.getElementById('desc').value;
    mainPhoto();
    result['photos_id'] = photos_id;
    result['other_photos'] = other_photos;
    result['main_photo'] = main_photos;
    result['description'] = desc;

    xhttp.open('Post', '/products/info/update/' + id, true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send(JSON.stringify(result));
    xhttp.onreadystatechange = function () {
        if ((this.readyState ==4) && (this.status == 200)){
            console.log(this.responseText);
        }
    }

}

function otmenFunction() {

    const value = window.location.href.substr(window.location.href.lastIndexOf('/') + 1);

    window.open('/products/info/get/' + value, '_self');
}

function deletePhoto(e) {
    let result = confirm("Действительно удалить?");

    let img_id = e.previousElementSibling.firstElementChild.id;
    console.log(e.previousElementSibling.firstElementChild.id);
    if (result){
        xhttp.open('delete', '/products/photo/delete/' + img_id, true);
        xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
        xhttp.send();
        xhttp.onreadystatechange = function () {
            if ((this.readyState ==4) && (this.status == 200)){
                let resp = JSON.parse(this.responseText);
                console.log(resp);
                if (resp['success'] == true){
                    location.reload();
                }else {
                    alert(resp['comment']);
                }
            }
        }
    }
}

const fileSelect = document.getElementById("fileSelect"),
    fileElem = document.getElementById("fileElem");

fileSelect.addEventListener("click", function (e) {
    if (fileElem) {
        fileElem.click();
    }

}, false);


const full_div_other_photo = document.getElementById('full_div_other_photo');
const div_other_photo = document.getElementById('div_other_photo');
let base_64_code = [];
let requestJson = {}

function addPhoto() {
   const con = confirm("Сохранить изображение?");

   if (con == true) {
       xhttp.open('Post', '/products/photo/add', true);
       xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");

       xhttp.send(JSON.stringify(requestJson));
       xhttp.onreadystatechange = function () {
           if ((this.readyState == 4) && (this.status == 200)) {
               let resp = JSON.parse(this.responseText);
               if (resp['success']) {
                   location.reload()
               }
           }
       }
   }
}

function set_other_photos(ev) {
    base_64_code = [];
    requestJson =  readURL(ev, div_other_photos);
}

function readURL(ev, parent_div) {
    let main = [];
    let oth_photos = [];
    if (ev.files && ev.files[0]) {
        for (let i = 0; i < ev.files.length; i++) {
            if (ev.files[i].size <= 100000) {
                let reader = new FileReader();
                reader.onload = function (e) {
                    let img = document.createElement('img');
                    let button = document.createElement('BUTTON');
                    let div2 = document.createElement('DIV');
                    let div1 = document.createElement('DIV');
                    button.textContent = 'Удалить фото';

                    div1.setAttribute('class','full-div-other-photo')
                    div1.setAttribute('id','full_div_other_photo')

                    div2.setAttribute('class','div-other-photo')
                    div2.setAttribute('id','div_other_photo')

                    button.setAttribute('type','button')
                    button.setAttribute('class','delete-photo')
                    button.setAttribute('onclick','deletePhoto(this)')

                    img.setAttribute('src', e.target.result);
                    oth_photos.push(e.target.result)
                    img.setAttribute('main','False');
                    main.push('False')
                    img.setAttribute('onclick','changeMainPhoto(this);');

                    div2.appendChild(img);
                    div1.appendChild(div2);
                    div1.appendChild(button);
                    parent_div.appendChild(div1);
                    base_64_code.push(e.target.result);
                    // s.innerHTML = "<img src = '" + base_64_code[0] + "' width = '100%'>"
                }
                reader.readAsDataURL(ev.files[i]);
            }else {
                alert("Kiritilgan rasm 100kb dan katta bo'lmasligi kerak");
            }

        }
    }
    return {
        'main_photo' : main,
        'other_photos' : oth_photos,
        'product_id' : id
    }
}