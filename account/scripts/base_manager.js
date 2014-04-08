

$(function() {

    var $sidebar   = $("#sidebar"),
        $window    = $(window),
        offset     = $sidebar.offset(),
        topPadding = 15;

    $window.scroll(function() {
        if ($window.scrollTop() > 1) {
            $sidebar.stop().animate({
                marginTop: -$window.scrollTop()
            });
        } else {
            $sidebar.stop().animate({
                marginTop: 0
            });
        }
        if ($window.scrollTop() > 122) {
            $sidebar.stop().animate({
                marginTop: 0 - offset.top - topPadding
            });
            console.log($window.scrollTop());
            console.log(offset.top);
            console.log(topPadding);
        }
    });
    
});