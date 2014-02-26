





//This calls the ajax based on the change in the "username" textbox
$('#id_username').change(function (event) {

    var user = $('#id_username').val();

    $().load('/account/newuser/'+user+'/');
    console.log('/account/newuser/'+user+'/');
                
});








//This calls the ajax based on the change in the "username" textbox
// $('#id_username').change(function (event) {

//         console.log('it changed!!');

//         $.get('/newuser/', {username: $('#id_username').val()}, function (data){
//                 if (data == "True") {
//                     $('#idVal').html("You may use this ID");
//                 } else {
//                     $('#idVal').html("Unavailable");
//                 }

//         });
// });