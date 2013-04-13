$(document).ready(init)

function init(){
    $("#submit").click(submit);
}

function submit(){
    var cid = $("#id").val();
    $.post("/ajax", {"cid" : cid}, function(data){
        $("#output textarea").val(data);
    });
}