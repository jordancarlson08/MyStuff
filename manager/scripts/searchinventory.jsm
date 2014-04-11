

jQuery(document).ready(function($) {
    $(".clickableRow").click(function() {
          window.document.location = $(this).attr("href");
    });
});


$(function() {
    var hash = window.location.hash;
    hash && $('ul.nav a[href="' + hash + '"]').tab('show');
});
	



%for i in rental:
$(function() {

  $('#rent_${i.id}').off('click.add').on('click.add', function(){

	$('#rent_${i.id}').animate({
		'left':'0px',
		width: '141px',
		height:'34px',
	});
	$('#rent_${i.id}').html('<span class="glyphicon glyphicon-ok"></span>&nbsp; Added to Cart!');
	$('#tr_${i.id}').css('text-decoration','line-through');


	//Add the rental to the cart

	console.log('/catalog/cart__add/${i.id}/1/rental/');
	$.ajax({
		type: "POST",
		url: '/catalog/cart__add/${i.id}/1/rental/',
	});

  });

	// 	var isClicked = false;

	// $('#title_${i.id}').off('click.add').on('click.add', function(){



	// 	if (isClicked === false)
	// 	{
	// 		$('#title_${i.id}').html('<span class="glyphicon glyphicon-minus"></span>&nbsp;');
	// 		isClicked= !isClicked;
	// 		return isClicked;
	// 	}
	// 	else
	// 	{
	// 		$('#title_${i.id}').html('<span class="glyphicon glyphicon-plus"></span>&nbsp;');
	// 		isClicked= !isClicked;
	// 		return isClicked;
	// 	}

	// });

	// $('#collapse_${i.id}').on('hidden.bs.collapse', function () {
	// 	console.log("hidden!!!");
	// });
	// $('#collapse_${i.id}').on('show.bs.collapse', function () {
	// 	console.log("Show!!!");
	// });




});
%endfor

$(function() {

	//This sorts the list by manufacturer
	$('#select_man').change(function(event) {
		var url = '/manager/searchinventory/';
		var value = ($('#select_man').val());
		var url2;
		if (value === 'A - Z'){
			url2 = 'manufacturer/';
		} else if (value == 'Z - A') {
			url2 = 'manufacturer/-';
		} else {
			url2 = '';
		}

		var newurl = url+url2;
		window.location.href = newurl;
	});


	$('#select_name').change(function(event) {
		var url = '/manager/searchinventory/';
		var value = ($('#select_name').val());
		var url2;
		if (value === 'A - Z'){
			url2 = 'name/';
		} else if (value == 'Z - A') {
			url2 = 'name/-';
		} else {
			url2 = '';
		}

		var newurl = url+url2;
		window.location.href = newurl;
	});

	$('#select_price').change(function(event) {
		var url = '/manager/searchinventory/';
		var value = ($('#select_price').val());
		var url2;
		if (value === 'Low - High'){
			url2 = 'listPrice/';
		} else if (value == 'High - Low') {
			url2 = 'listPrice/-';
		} else {
			url2 = '';
		}

		var newurl = url+url2;
		window.location.href = newurl;
	});

	$('#select_cost').change(function(event) {
		var url = '/manager/searchinventory/';
		var value = ($('#select_cost').val());
		var url2;
		if (value === 'Low - High'){
			url2 = 'cost/';
		} else if (value == 'High - Low') {
			url2 = 'cost/-';
		} else {
			url2 = '';
		}

		var newurl = url+url2;
		window.location.href = newurl;
	});

	$('#select_cat').change(function(event) {
		var url = '/manager/searchinventory/';
		var value = ($('#select_cat').val());
		var url2;
		if (value === 'A - Z'){
			url2 = 'category/';
		} else if (value == 'Z - A') {
			url2 = 'category/-';
		} else {
			url2 = '';
		}

		var newurl = url+url2;
		window.location.href = newurl;
	});

	$('#select_views').change(function(event) {
		var url = '/manager/searchinventory/';
		var value = ($('#select_views').val());
		var url2;
		if (value === 'Low - High'){
			url2 = 'views/';
		} else if (value == 'High - Low') {
			url2 = 'views/-';
		} else {
			url2 = '';
		}

		var newurl = url+url2;
		window.location.href = newurl;
	});

});
