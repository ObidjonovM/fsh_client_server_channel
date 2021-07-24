function otmenFunction() {

    const value = location.href.substr(
        location.href.lastIndexOf('/') + 1
    );

    window.open('/carrier/get/' + value, '_self');
}
