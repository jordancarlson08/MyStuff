


//Ajax call, basic example
$(function() {

	$('#login_button2').off('click.login').on('click.login', function(){

		$('#login_button').loadmodal({
			url: '/account/login/',
			id: 'login_modal2',
			title: '<h2>Login</h2>',
			width: '600px',
			ajax: {
				dataType: 'html',
				method: 'POST',
				success: function(data, status, xhr) {
					console.log($('#login_modal2'));
				},//
			// any other options from the regular $.ajax call (see JQuery docs)
			
			},
		});
	});

	// for ( var i = 0; i < 10; i++ ) {
	// 	$('#down_arrow').fadeTo(2000,1);
	// 	$('#down_arrow').fadeTo(2000,0.2);
	// }
});
