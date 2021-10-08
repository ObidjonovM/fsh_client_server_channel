const sm_photo_li = document.querySelectorAll('.sm-photo-li');
const org_photo_div = document.querySelectorAll('.org-photo-div');

for (let i = 0; i < sm_photo_li.length; i++) {

    sm_photo_li[i].addEventListener('click', function () {

        org_photo_div[i].classList.toggle('show');
        console.log('1')

    })

}