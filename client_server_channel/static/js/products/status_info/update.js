function otmenFunction() {

    const value = location.href.substr(
        location.href.lastIndexOf('/') + 1
    );

    window.open('/products/status/get/' + value, '_self');
}
