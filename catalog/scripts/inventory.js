


//Ajax call, basic example
$(function() {

	$('#gettime_button').off('click.gettime').on('click.gettime', function(){

		console.log('This should work');

		$('#gettime_button').loadmodal({
			url: '/account/login/',
			title: 'Login',
			width: '600px',


		}); //End Ajax
	});
});