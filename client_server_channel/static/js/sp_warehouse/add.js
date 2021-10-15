window.addEventListener( "load", function () {

    function sendData() {

        const XHR = new XMLHttpRequest();

        const FD = new FormData( form );

        XHR.addEventListener( "load", function(event) {

            if(event.target.responseURL == window.location.href){
                const resp = JSON.parse(event.target.responseText);
                if(resp.log_code == -1){
                    alert('Данная должность уже сушествует');
                }
            }else {
                location.href = event.target.responseURL;
            }
        } );

        XHR.addEventListener( "error", function( event ) {
            alert( 'Error' );
        } );

        XHR.open( "POST", "/sp_warehouse/add" );

        XHR.send( FD );
    }

    const form = document.getElementById( "myForm" );

    form.addEventListener( "submit", function ( event ) {
        event.preventDefault();
        console.log("1")
        sendData();
    } );
} );


function otmenFunction (){
    window.open('/sp_warehouse/all', '_self');
}

