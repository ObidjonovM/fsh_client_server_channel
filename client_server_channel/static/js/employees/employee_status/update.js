function otmenFunction(){
    const value = location.href.substr(
    		    location.href.lastIndexOf('/') + 1
		  );
    
    window.open('/employees/status/get/' + value, '_self');
}
