$(document).ready(function(){

    $("#slideToggle").click(function(){
      $("p").slideToggle("slow");
    });
    $("#fadeOut").click(function(){
      $("h1").fadeOut();
        });
    $("#fadeIn").click(function(){
      $("h1").fadeIn();
      });
    $("h3").hide(1000, function(){
      });
    $("#show").click(function(){
      $("h3").show();
      });
    $("#alert").click(function(){
      alert("OH YES!");
      });
    $("#toggle").click(function(){
      $("h4").toggle("slow", function(){
        //Animation complete;
        });
      });
    $("#slideUp").click(function(){
      $("h2").slideUp("slow", function(){
        //Animation complete;
        });
      });
    $("#slideDown").click(function(){
      $("h2").slideDown("slow", function(){
        //Animation complete;
      });
    });
    $("p").addClass("red");
    $("div").before("YO!");
    $("h2").after(" !word! ")
    $(".append").append(" Oh, and purple!");
    $("p.check").html("Don't doubt me!");
    $("#gender").click(function(){
    var gender = $("input[type=radio][name=gender]:checked").val();
    console.log(gender);
    alert("Thank you!");
  });
    $("img").attr({height:100,width:100});
    $("#data").click(function(){
    $("h2").text("Watch");
    });
    $(".append").data("red");
});
