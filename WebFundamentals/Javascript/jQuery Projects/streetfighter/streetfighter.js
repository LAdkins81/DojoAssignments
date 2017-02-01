$(document).ready(function(){

      $("button").hover(function(){
      var img = 'url(' + $(this).attr('data-bg-img') + ')';
      $('body').css("background-image", img);
      });

      $("button").click(function(){
      var img = 'url(' + $(this).attr('data-bg-img') + ')';
      $('body').css("background-image", img);
      $('#wrapper').css("display", 'none');
      $('#wrapper2').css("display", 'block');
      });

      $('#ninja').change(function(){
        var imageSource = $(this).find(':selected').data('picture');
        if(imageSource) {
          $('#ninjaplayers1').html('<img src="'+imageSource+'">');
          }
        else {
          $('#ninjaplayers1').html('');
          }
        });
        $('#ninja1').change(function(){
          var imageSource = $(this).find(':selected').data('picture');
          if(imageSource) {
            $('#ninjaplayers2').html('<img src="'+imageSource+'">');
            }
          else {
            $('#ninjaplayers2').html('');
            }
          });

      });
