$(function(){
    $(".edite").click(function(){
        com_id = jQuery(this).val();
        com_core = $("#"+com_id).text();
        event_token = $("#event_token").val();
        $("#"+com_id).replaceWith(
            '<form method="POST" action="/events/'+event_token+'/commentaire/edit/'+com_id+'" >'+
                '<input type="text" name="core" value="'+com_core+'"/>'+
                '<input type="submit" value="edite"/>'+
                '<input type="hidden" name="csrfmiddlewaretoken" value="'+SCRF_TOKEN+'"/>'+
            '</form>'
        );
    })

    $(".answer").click(function(){
        father = jQuery(this).val();
        event_token = $("#event_token").val();
        jQuery(this).replaceWith(
            '<form method="POST" action="/events/'+event_token+'/commentaire/" >'+
                '<input type="text" name="core"/>'+
                '<input type="submit" value="edite"/>'+
                '<input type="hidden" name="csrfmiddlewaretoken" value="'+SCRF_TOKEN+'"/>'+
                '<input type="hidden" name="father" value="'+father+'"/>'+
            '</form>'
        );
    })
})