function otmenFunction() {
    window.open('/clients/account', '_self');
}


const allInputs = document.querySelectorAll('input')

for(let i=0; i<allInputs.length; i++){
    if (allInputs[i].defaultValue == 'None') {
        allInputs[i].defaultValue = '';
    }
}
