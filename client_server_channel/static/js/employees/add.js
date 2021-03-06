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

        XHR.open( "POST", "/employees/add" );

        XHR.send( FD );
    }

    const form = document.getElementById( "myForm" );

    form.addEventListener( "submit", function ( event ) {
        event.preventDefault();

        sendData();
    } );
} );


function otmenFunction (){
    window.open('/employees/all', '_self');
}

function отдельFunction (){
    window.open('/employees/department/all', '_self');
}

function типFunction (){
    window.open('/employees/type/all', '_self');
}

function статусFunction (){
    window.open('/employees/status/all', '_self');
}
