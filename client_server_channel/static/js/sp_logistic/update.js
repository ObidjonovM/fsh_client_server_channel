function otmenFunction() {

    const value = location.href.substr(
        location.href.lastIndexOf('/') + 1
    );

    window.open('/sp_logistic/get/' + value, '_self');
}
