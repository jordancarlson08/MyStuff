

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



});