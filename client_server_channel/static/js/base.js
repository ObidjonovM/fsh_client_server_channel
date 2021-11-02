function glavniyStranisa(ev){
    window.open('/', '_self');
    ev.removeAttribute("href");
}

function Viyti(ev) {
    window.open('/employees/logout', '_self');
    ev.removeAttribute("href");
}

function Logout(ev) {
    window.open('/clients/logout', '_self');
    ev.removeAttribute("href");
}

var allEl = document.querySelectorAll('*');
[].forEach.call(allEl, function(allEl) {
    if ('None'.includes(allEl.innerHTML)) {
        allEl.innerHTML = '';
    }
})

let inputss = document.querySelectorAll('input');
for (let i=0; i<inputss.length; i++){
    if (inputss[i].value === 'None'){
        inputss[i].value = '';
    }
}
