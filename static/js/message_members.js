$(function(){
    $(".target").click(function(){
        var target = $(this).val();

        $.ajax({
            url:'/compte/ajax/getmessage/',
            data: {
                'author_id': target
            },
            datatype: 'json',
            success: function(data){
                var data = $.parseJSON(data)
                var div_message = "<div id=\"messages\">";
                for(var k in data){
                    for(var k_2 in data[k]){
                        if(k_2 == 'fields'){
                            div_message += '<div style="border: 1px solid green">'+
                                                '<p>'+data[k][k_2]['content']+'</p>'+
                                                '<p style="font-size: 10px; color: grey">'+data[k][k_2]['date']+'</p>'+
                                            '</div>';
                        }
                    }
                }
                div_message += "<form method=\"POST\" action=\"/compte/message/send/\" id=\"send_mess\">"+
                                    "<textarea id=\"content\" name=\"content\" class=\"input\" required=\"\" rows=\"10\" placeholder=\"Message...\" cols=\"40\" id=\"id_content\" maxlength=\"600\"></textarea>"+
                                    '<input type="hidden" name="csrfmiddlewaretoken" value="'+SCRF_TOKEN+'"/>'+
                                    "<input type=\"hidden\" value=\""+target+"\" name=\"author_id\" />"+
                                    '<input type="submit" value="Envoyer"/>'+
                                "</form>"+
                            "</div>";
                $('#messages').replaceWith(div_message);
            }
        });
    });

    $("#send_mess").submit(function(e){
        e.preventDefault(); // marche pas je sais pas pq...
        $.ajax({
            url: '/compte/message/send/',
            type: "POST",
            datatype: "html",
            success: function(response){
                $("#messages").append("<div style=\"border: 1px solid green\">"+
                                        "<p>"+$("#content").val()+"</p>"+
                                        "<p>sended</p>"+
                                    "</div>");
            },
        });
    });
});