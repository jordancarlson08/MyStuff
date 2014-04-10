
//This calls the ajax based on the change in the "username" textbox
$('#id_username').change(function (event) {

    var user = $('#id_username').val();

    $().load('/account/newuser/'+user+'/');
    console.log('/account/newuser/'+user+'/');
                
});
