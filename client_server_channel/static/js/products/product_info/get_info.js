const sm_photo_li = document.querySelectorAll('.sm-photo-li');
const org_photo_div = document.querySelectorAll('.org-photo-div');



function smPhotoLi(x){
    x.style.border = '1px solid #1b232e';
}

for (let i=0; i<sm_photo_li.length; i++){

    sm_photo_li[i].addEventListener('click', function (){
        if (org_photo_div[i].style.display == 'block'){
            console.log(org_photo_div[i]);
            org_photo_div[i].classList.add('active1');
        }else {
            console.log(org_photo_div[i]);
            org_photo_div[i].classList.remove('active1');
        }



    })
}


function displayBlock(e){
    const block = document.createElement('P');
}