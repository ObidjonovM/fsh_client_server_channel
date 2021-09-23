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


