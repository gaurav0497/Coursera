$(function (){
	// equal to document.Queryselector(#elemet).blur
	$("#navbarToggle").blur( function(event){

		var screen = window.innerWidth;
		if(screen<768){
		$("#navbarSupportedContent").collapse('hide');
		}

	});

	$("#navbarToggle").click(function (event) {
    		$(event.target).focus();
  });

}); // for hiding toggle button when not in use 



