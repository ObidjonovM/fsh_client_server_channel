const sm_photo_li = document.querySelectorAll('.sm-photo-li');
const org_photo_div = document.querySelectorAll('.org-photo-div');
let a = 1;

// for (let i = 0; i < sm_photo_li.length; i++) {

sm_photo_li[0].addEventListener('click', function () {
    console.log(org_photo_div[0]);
    if (org_photo_div[0]) {
        if (org_photo_div[0].style.display != 'block') {
            sm_photo_li[0].classList.add('show2');
            sm_photo_li[1].classList.remove('show2');
            sm_photo_li[2].classList.remove('show2');
            sm_photo_li[3].classList.remove('show2');
            sm_photo_li[4].classList.remove('show2');

            org_photo_div[0].style.display = 'block';
            org_photo_div[1].style.display = 'none';
            org_photo_div[2].style.display = 'none';
            org_photo_div[3].style.display = 'none';
            org_photo_div[4].style.display = 'none';

        } else {
            sm_photo_li[0].classList.remove('show2');
            // org_photo_div[0].style.display = 'none';
        }
    }


})

sm_photo_li[1].addEventListener('click', function () {
    if (org_photo_div[1]) {
        if (org_photo_div[1].style.display != 'block') {
            sm_photo_li[0].classList.remove('show2');
            sm_photo_li[1].classList.add('show2');
            sm_photo_li[2].classList.remove('show2');
            sm_photo_li[3].classList.remove('show2');
            sm_photo_li[4].classList.remove('show2');

            org_photo_div[1].style.display = 'block';
            org_photo_div[0].style.display = 'none';
            org_photo_div[2].style.display = 'none';
            org_photo_div[3].style.display = 'none';
            org_photo_div[4].style.display = 'none';

        } else {
            sm_photo_li[1].classList.remove('show2');
            // org_photo_div[1].style.display = 'none';
        }
    }
})

sm_photo_li[2].addEventListener('click', function () {
    if (org_photo_div[2]) {
        if (org_photo_div[2].style.display != 'block') {
            sm_photo_li[0].classList.remove('show2');
            sm_photo_li[1].classList.remove('show2');
            sm_photo_li[2].classList.add('show2');
            sm_photo_li[3].classList.remove('show2');
            sm_photo_li[4].classList.remove('show2');

            org_photo_div[2].style.display = 'block';
            org_photo_div[0].style.display = 'none';
            org_photo_div[1].style.display = 'none';
            org_photo_div[3].style.display = 'none';
            org_photo_div[4].style.display = 'none';

        } else {
            sm_photo_li[2].classList.remove('show2');
            // org_photo_div[2].style.display = 'none';
        }
    }
})

sm_photo_li[3].addEventListener('click', function () {
    if (org_photo_div[3]) {
        if (org_photo_div[3].style.display != 'block') {
            sm_photo_li[0].classList.remove('show2');
            sm_photo_li[1].classList.remove('show2');
            sm_photo_li[2].classList.remove('show2');
            sm_photo_li[3].classList.add('show2');
            sm_photo_li[4].classList.remove('show2');

            org_photo_div[3].style.display = 'block';
            org_photo_div[0].style.display = 'none';
            org_photo_div[1].style.display = 'none';
            org_photo_div[2].style.display = 'none';
            org_photo_div[4].style.display = 'none';

        } else {
            sm_photo_li[3].classList.remove('show2');
            // org_photo_div[3].style.display = 'none';
        }
    }
})

sm_photo_li[4].addEventListener('click', function () {
    if (org_photo_div[4]) {
        if (org_photo_div[4].style.display != 'block') {
            sm_photo_li[0].classList.remove('show2');
            sm_photo_li[1].classList.remove('show2');
            sm_photo_li[2].classList.remove('show2');
            sm_photo_li[3].classList.remove('show2');
            sm_photo_li[4].classList.add('show2');

            org_photo_div[4].style.display = 'block';
            org_photo_div[0].style.display = 'none';
            org_photo_div[1].style.display = 'none';
            org_photo_div[2].style.display = 'none';
            org_photo_div[3].style.display = 'none';

        } else {
            sm_photo_li[4].classList.remove('show2');
            // org_photo_div[4].style.display = 'none';
        }
    }
})


// }
