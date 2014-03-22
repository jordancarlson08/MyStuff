


//Ajax call, basic example
$(function() {

	$('#login_button2').off('click.login').on('click.login', function(){

		$('#login_button2').loadmodal({
			url: '/account/login/',
			id: 'login_modal',
			title: '<h2>Login</h2>',
			width: '600px',
			ajax: {
				dataType: 'html',
				method: 'POST',
				success: function(data, status, xhr) {
					console.log($('#login_modal'));
				},//
			// any other options from the regular $.ajax call (see JQuery docs)
			
			},
		});
	});
});
