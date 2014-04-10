

$(function() {

	$('form').ajaxForm();

	$('#add_button').off('click.add').on('click.add', function(){


		$('#add_button').animate({
			width: '141px',
			height:'34px'
		});
		$('#add_button').html('<span class="glyphicon glyphicon-ok"></span>&nbsp; Added to Cart!');

	});


});




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


$(function() {

	$('td').mouseenter(function(){

		$('tr').each(function(){
			console.log('tr');

		});


	});


});