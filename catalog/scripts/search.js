

// $(document).ready(function ()
//   {
//       $('#ajax1').click(function ()
//           {
//               $('.list-inline').load('/catalog/search_results/');

//           });
//   });
$(function() {

	//This calls the ajax based on the change in the "brand" combo box
	$('#brand').change(function(event) {
		var url = '/catalog/search__results/';
		var url2 = $('#brand').val();
		var newurl = url+url2;
		//console.log(newurl);
		// $('.list-inline').load('/catalog/search_results/');
		$('.list-inline').load(newurl);

	});

});

// jQuery(document).ready(function($) {
//       $(".clickableRow").click(function() {
//             window.document.location = $(this).attr("href");
//       });
// });