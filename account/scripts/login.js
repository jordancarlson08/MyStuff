

//Not working... on the modal... works on a normal page
$(function() {

	$("#the_button").on('click.the_button', function(){
		console.log("this is here");
		$.ajax({

			url:"/index/",
			success:function(result){
				$("#here").html(result);
		}});
	});
});









