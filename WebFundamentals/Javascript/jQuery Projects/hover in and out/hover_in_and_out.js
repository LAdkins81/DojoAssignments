$(document).ready(function(){
        $("img").attr({height:250,width:250});

        var first = "";
        $("img").hover(function(){
          first = $(this).attr("src");
          $(this).attr("src", $(this).attr("data-alt-src"));
      }, function(){
        $(this).attr("src",first);

      });
    });
