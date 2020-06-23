$(function (){
	$("#navbarToggle").blur( function(event){
		var screen = window.innerWidth;
		if(screen<768){
		$("#navbarSupportedContent").collapse('hide');
		}

	});

	});
