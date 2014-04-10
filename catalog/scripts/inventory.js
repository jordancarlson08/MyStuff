


$(function() {

	$('#img').click(function() {
		var clicks = $(this).data('clicks');
		if (clicks) {

			$('#img').animate({
				width:'600px'
			});

		} else {

			$('#img').animate({
				width:'300px'
			});
		}
		$(this).data("clicks", !clicks);
	});

	$('#img').css( 'cursor', 'pointer' );

	$('#zoom').click(function() {
		var clicks = $(this).data('clicks');
		if (clicks) {

			$('#img').animate({
				width:'600px'
			});

		} else {

			$('#img').animate({
				width:'300px'
			});
		}
		$(this).data("clicks", !clicks);
	});

	$('#zoom').css( 'cursor', 'pointer' );

});

$(function() {
	
	$('#add_button_disabled').mouseenter(function(){
		console.log('Mouseover disabled');

		$('#add_button_disabled').animate({

			width:'600px'


		});

	});

	$('#add_button_disabled').mouseleave(function(){

		$('#add_button_disabled').animate({

			width:'300px'


		});

	});

});

$(function() {

	$('#back_button').off('click.back').on('click.back', function(){
		history.go(-1);

	});

});

