$(function() {

	$('#back_button').mouseenter(function(){

		$('#back_button').css({
			color:'red'
		});

	});
	$('#back_button').mouseleave(function(){


		$('#back_button').css({
			color:'black'
		});

	});


	$('#back_button').off('click.back').on('click.back', function(){
		history.go(-1);

	});

});