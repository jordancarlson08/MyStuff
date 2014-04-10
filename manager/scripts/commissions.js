
$(function() {

	//This calls the ajax based on the change in the combo box
	$('#emp').change(function(event) {
		var url = '/manager/commissions__get/';
		var url2 = $('#emp').val();
		var newurl = url+url2;
		console.log(newurl);

		$('.commissions-list').load(newurl);

	});

});
