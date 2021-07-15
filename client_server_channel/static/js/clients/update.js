function otmenFunction() {

    const value = location.href.substr(
        location.href.lastIndexOf('/') + 1
    );

    window.open('/clients/get/' + value, '_self');
}
