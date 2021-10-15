let link_all = document.querySelectorAll('.link-all');

for (let i=0; link_all.length; i++){
    link_all[i].addEventListener('focus', function () {
        link_all[i].style.backgroundColor = 'black';
    })

}
