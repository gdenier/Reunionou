function getNotif(){
    $.ajax({
        url:'/members/ajax/getnotif/',
        data: {
            'ajax': 'true',
        },
        datatype: 'json',
        type: 'GET',
        success: function(data){
            
        }
    });
    setTimeout('getNotif', 10000);
}

getNotif();