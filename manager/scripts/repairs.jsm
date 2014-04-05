

jQuery(document).ready(function($) {
    $(".clickableRow").click(function() {
          window.document.location = $(this).attr("href");
    });
});



%for r in repairs:
$(function() {

  $('#add_button_${r.id}').off('click.add').on('click.add', function(){

	$('#add_button_${r.id}').animate({
		'left':'0px',
		width: '141px',
		height:'34px',
	});
	$('#add_button_${r.id}').html('<span class="glyphicon glyphicon-ok"></span>&nbsp; Added to Cart!');

	//Add the rental to the cart

	console.log('/catalog/cart__add/${r.id}/1/repair/');
	$.ajax({
		type: "POST",
		url: '/catalog/cart__add/${r.id}/1/repair/',
		
	});
  });

  $('#complete_button_${r.id}').off('click.add').on('click.add', function(){

	$('#complete_button_${r.id}').html('<span class="glyphicon glyphicon-check"></span>');
	console.log('/manager/repairs__complete/${r.id}/');
	$.ajax({
		type: "POST",
		url: '/manager/repairs__complete/${r.id}/',
		
	});
  });


});
%endfor

$(function() {



});