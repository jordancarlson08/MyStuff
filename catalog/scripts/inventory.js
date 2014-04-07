

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

	$('#img').mouseenter(function(){

		$('#img').animate({

			width:'600px'


		});

	});

	$('#img').mouseleave(function(){

		$('#img').animate({

			width:'300px'


		});

	});

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


$(function() {

	$('td').mouseenter(function(){

		$('tr').each(function(){
			console.log('tr');

		});


	});


});