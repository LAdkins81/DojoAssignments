$(document).ready(function(){
  
          $("img").attr({height:250,width:250});

          $("img").click(function(){
              $(this).hide();
          });
          $("input").click(function(){
              $("img").show();
          });
      });
