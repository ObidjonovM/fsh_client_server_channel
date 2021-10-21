function glavniyStranisa(){
    window.open('/', '_self');
}

function Viyti() {
    window.open('/employees/logout', '_self');
}

function Logout() {
    window.open('/clients/logout', '_self');
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
