function otmenFunction (){
    window.open('/products/info/all', '_self');
}

const div_main_photo = document.getElementById('div_main_photo');
const div_other_photos = document.getElementById('div_other_photos');
const other_photos = document.getElementById('other_photos');



let base_64_code = [];
function set_other_photos(ev) {
    base_64_code = [];
    div_main_photo.innerHTML = '';
    div_other_photos.innerHTML = '';
    readURL(ev, div_other_photos);
}


function readURL(ev, parent_div) {
    if (ev.files && ev.files[0]) {
        for (let i = 0; i < ev.files.length; i++) {
            if (ev.files[i].size <= 100000) {
                let reader = new FileReader();
                reader.onload = function (e) {
                    let img = document.createElement('img');
                    img.setAttribute('src', e.target.result);
                    img.setAttribute('width', '30%');
                    parent_div.appendChild(img);
                    base_64_code.push(e.target.result);
                    div_main_photo.innerHTML = "<img src = '" + base_64_code[0] + "' width = '30%'>"
                }
                reader.readAsDataURL(ev.files[i]);
            }else {
                alert("Kiritilgan rasm 100kb dan katta bo'lmasligi kerak");
            }

        }
    }

}

function get_photos(imgs) {
    let result = []
    for (let i = 0; i < imgs.length; i++) {
        result.push(imgs[i].currentSrc)
    }

    return result
}

function get_main_photos (otherImg, mainImg) {
    let result = [];
    for (let i=0; i<otherImg.length; i++){
        if (mainImg[0] == otherImg[i]){
            result.push(true);
        }else {
           result.push(false);
        }
    }
    return result;
}


const xhttp = new XMLHttpRequest();
function addForm() {
    let info = {};
    let src_other_photos = get_photos(div_other_photos.children);
    let src_main_photo = get_photos(div_main_photo.children);
    const name = document.getElementById('name');
    const model = document.getElementById('model');
    const cat_id = document.getElementById('cat_id');
    const desc = document.getElementById('desc');
    info['name'] = name.value;
    info['model'] = model.value;
    info['cat_id'] = cat_id.value;
    info['main_photo'] = get_main_photos(src_other_photos, src_main_photo);
    info['other_photos'] = src_other_photos;
    info['desc'] = desc.value;
    xhttp.open('POST', '/products/info/add', true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send(JSON.stringify(info));

    xhttp.onreadystatechange = function() {

        if (xhttp.readyState == 4 && xhttp.status == 200) {
            const resp = JSON.parse(xhttp.responseText);
            if (resp['success']) {
                window.location.href = '/products/info/all';
            }else {
                alert(resp['comment'])
            }

        }
    }


}