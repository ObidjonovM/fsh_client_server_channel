function otmenFunction() {

    const value = location.href.substr(
        location.href.lastIndexOf('/') + 1
    );

    window.open('/supplier/get/' + value, '_self');
}
