$(document).ready(init)

function init(){
    var i = $("#output textarea");
    i.css("height", $(window).height() - $("#input").height() - 50);
    i.css("width", $("#input").width() - 50);
    i.click(function(){
        this.focus();
        this.select();
    });
    $("#id").bind("keyup", function(e){
        if (e.keyCode == "13"){
            submit();
        }
    });
    $("#submit").click(submit);
}

function submit(){
    var cid = $("#id").val();
    $.post("/ajax", {"cid" : cid}, function(data){
        $("#output textarea").val(data);
    });
}