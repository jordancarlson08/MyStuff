

$(function() {

  $('form').ajaxForm();

  $('#add_button').off('click.add').on('click.add', function(){

	$('#add_button').animate({
		width: '135px',
		height:'40px'
	});
	$('#add_button').animate({
		width: '120px',
		height:'34px'
	});

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