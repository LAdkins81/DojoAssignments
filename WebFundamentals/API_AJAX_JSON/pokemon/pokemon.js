
$(document).ready(function(){
    //  use javascript and jquery to add the img, loop, and add the image to the html;
    for(var i=1; i<152; i++){
      $("#pokeimgs").append('<img id='+i+' src="http://pokeapi.co/media/img/'+i+'.png">');
    };

    $(document).on("click", "img", function(){
        var idnum = $(this).attr("id");
        var imgurl = "http://pokeapi.co/media/img/" + idnum + ".png";
        var url = "http://pokeapi.co/api/v1/pokemon/" + idnum;
        console.log("hi");
       $.get(url, function(res){
         $("#pokedex h2").html(res.name);
         $("#pokedex #type").html(res.types[0].type.name);
         $("#pokedex #height").html(res.height);
         $("#pokedex #weight").html(res.weight);
         $("#pokedex img").attr('src',imgurl);
       },
       "json");
        });
      });
