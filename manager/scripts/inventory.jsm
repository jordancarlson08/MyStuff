


$(function () {
    $('#myTab a:last').tab('show');
});

jQuery(document).ready(function($) {
      $(".clickableRow").click(function() {
            window.document.location = $(this).attr("href");
      });
});



