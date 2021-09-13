// window.addEventListener( "load", function () {
//     function sendData() {
//         const XHR = new XMLHttpRequest();

//         const FD = new FormData( form );

//         XHR.addEventListener( "load", function(event) {
//             // if(event.target.responseURL == window.location.href){
//             //     // const resp = JSON.parse(event.target.responseText);
//             //     // if(resp.log_code == -1){
//             //         alert('Данная должность уже сушествует');
//             //     // }
//             // }else {
//             //     location.href = event.target.responseURL;
//             // }
//             console.log(event)
//         } );

//         XHR.addEventListener( "error", function( event ) {
//             alert( 'Error' );
//         } );

//         XHR.open( "POST", "/products/info/add" );

//         XHR.send( FD );
//     }

//     const form = document.getElementById( "myForm" );

//     form.addEventListener( "submit", function ( event ) {
//         event.preventDefault();

//         sendData();
//     } );
// } );


// function otmenFunction (){
//     window.open('/products/info/all', '_self');
// }

const div_main_photo = document.getElementById('div_main_photo');
const div_other_photos = document.getElementById('div_other_photos');
const other_photos = document.getElementById('other_photos');



let base_64_code = []
function set_other_photos(ev) {
    base_64_code = []
    div_main_photo.innerHTML = ''
    div_other_photos.innerHTML = ''
    readURL(ev, div_other_photos);
};


function readURL(ev, parent_div) {
    if (ev.files && ev.files[0]) {
        for (let i = 0; i < ev.files.length; i++) {
            if (ev.files[i].size <= 100000) {
                let reader = new FileReader();
                reader.onload = function (e) {
                    let img = document.createElement('img');
                    img.setAttribute('src', e.target.result);
                    img.setAttribute('width', '20%');
                    parent_div.appendChild(img);
                    base_64_code.push(e.target.result);
                    div_main_photo.innerHTML = "<img src = '" + base_64_code[0] + "' width = '20%'>"
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



const xhttp = new XMLHttpRequest();
function addForm() {
    let info = {}
    let src_other_photos = get_photos(div_other_photos.children);
    let src_main_photo = get_photos(div_main_photo.children);
    const name = document.getElementById('name');
    const model = document.getElementById('model');
    const cat_id = document.getElementById('cat_id');
    info['name'] = name.value;
    info['model'] = model.value;
    info['cat_id'] = cat_id.value;
    info['main_photo'] = src_main_photo;
    info['other_photos'] = src_other_photos;
    xhttp.open('POST', '/products/info/add', true);
    xhttp.setRequestHeader("Content-type", "application/json; charset=UTF-8");
    xhttp.send(JSON.stringify(info));
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            const resp = JSON.parse(xhttp.responseText);
            if (resp['success']) {
                window.location.href = '/products/info/all'
            }else {
                alert(resp['comment'])
            }
        }
    }
}