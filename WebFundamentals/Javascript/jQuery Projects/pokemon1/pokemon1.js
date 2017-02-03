$(document).ready(function(){
    //  use javascript and jquery to add the img, loop, and add the image to the html;
    for(var i=1; i<152; i++){
      $("#pokemon").append('<img src="http://pokeapi.co/media/img/'+i+'.png">');
    };
  });
