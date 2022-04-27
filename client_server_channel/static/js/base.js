function glavniyStranisa(){
    window.open('/', '_self');
}

function Logout() {
    window.open('/clients/logout', '_self');
}

var allEl = document.querySelectorAll('*');
[].forEach.call(allEl, function(allEl) {
    if ('None'.includes(allEl.innerHTML)) {
        allEl.innerHTML = '';
    }
});

let inputss = document.querySelectorAll('input');
for (let i=0; i<inputss.length; i++){
    if (inputss[i].value === 'None'){
        inputss[i].value = '';
    }
}

// window.addEventListener("scroll", function(){
//     var header = document.querySelector(".add-button");
//     header.classList.toggle("sticky", window.scrollY > 0);
// });
//
// window.addEventListener("scroll", function(){
//     var fixed = document.querySelector(".fixed");
//     fixed.classList.toggle("sticky", window.scrollY > 0);
// });
//
// window.addEventListener("scroll", function(){
//     var thead = document.querySelector("thead");
//     thead.classList.toggle("sticky", window.scrollY > 0);
// });
