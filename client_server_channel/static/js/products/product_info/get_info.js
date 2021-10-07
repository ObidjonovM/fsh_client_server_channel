const sm_photo_li = document.querySelectorAll('.sm-photo-li');
const org_photo_div = document.querySelectorAll('.org-photo-div');

const small_text = document.getElementById('small_text');
const large_text = document.getElementById('large_text');

function smPhotoLi(x){
    small_text.style.display = 'block';
    large_text.style.display = 'none';
}

function smallImgClick(evt) {

        // e.target.classList.toggle('active1');
    // for (let i=0; i<org_photo_div.length; i++){

        if (evt.style.border == '1px solid #adaeb19e'){
            // evt.style.border = '1px solid #1b232e';
            evt.style.border = '1px solid #1b232e';
        }else {
            evt.style.border = '1px solid #adaeb19e';
            // evt.style.border = '1px solid #adaeb19e';
            // evt.nextElementSibling.style.border = "1px solid #adaeb19e";
            // evt.previousElementSibling.style.border = "1px solid #adaeb19e";
        }
    // }



    console.log("1")

}