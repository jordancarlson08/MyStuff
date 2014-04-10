


$(function () {
    $('#myTab a:last').tab('show');
});

jQuery(document).ready(function($) {
      $(".clickableRow").click(function() {
            window.document.location = $(this).attr("href");
      });
});

//Ajax call, basic example
$(function() {
	%for s in serial:
	$('#item_button_${s.id}').off('click.item').on('click.item', function(){

		$('#item_button_${s.id}').loadmodal({
			url: '/manager/item/${s.id}',
			id: 'item_modal_${s.id}',
			title: '<h2>Edit ${s.catalogItem.manufacturer} ${s.catalogItem.name} - ${s.serialNum}</h2>',
			width: '800px',
			ajax: {
				dataType: 'html',
				method: 'POST',
				success: function(data, status, xhr) {
					console.log($('#item_modal_${s.id}'));
				},//
			// any other options from the regular $.ajax call (see JQuery docs)
			
			},
		});
	});
	%endfor
});

