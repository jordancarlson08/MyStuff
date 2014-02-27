

//Ajax call, basic example
$(function() {

	$('#login_button').off('click.login').on('click.login', function(){

		console.log('This should work');

		$('#login_button').loadmodal({
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
