

//Ajax call, basic example
$(function() {

	$('#login_button').off('click.login').on('click.login', function(){

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


//Ajax call, basic example
$(function() {

	$('#cart_button').off('click.cart').on('click.cart', function(){
		console.log('2');
		$('#cart_button').loadmodal({
			url: '/catalog/cart/',
			id: 'cart_modal',
			title: '<h2>Shopping Cart</h2>',
			width: '600px',
			ajax: {
				dataType: 'html',
				method: 'POST',
				success: function(data, status, xhr) {
					console.log($('#cart_modal'));
				},//
			// any other options from the regular $.ajax call (see JQuery docs)
			
			},
		});
	});
});

