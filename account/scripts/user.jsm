

//Ajax call to create a modal
$(function() {

	$('#password_button').off('click.password').on('click.password', function(){

		$('#password_button').loadmodal({
			url: '/account/user__password/${user.id}',
			id: 'password_modal',
			title: '<h2>Edit Password</h2>',
			width: '600px',
			ajax: {
				dataType: 'html',
				method: 'POST',
				success: function(data, status, xhr) {
					console.log($('#password_modal'));
				},//
			// any other options from the regular $.ajax call (see JQuery docs)
			
			},
		});
	});
});

//Ajax call to create a modal
$(function() {

	$('#edit_button').off('click.edit').on('click.edit', function(){

		$('#edit_button').loadmodal({
			url: '/account/user__edit/${user.id}',
			id: 'edit_modal',
			title: '<h2>Edit Account Info</h2>',
			width: '600px',
			ajax: {
				dataType: 'html',
				method: 'POST',
				success: function(data, status, xhr) {
					console.log($('#edit_modal'));
				},//
			// any other options from the regular $.ajax call (see JQuery docs)
			
			},
		});
	});
});