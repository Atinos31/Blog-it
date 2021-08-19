  $(document).ready(function(){
    $('.sidenav').sidenav({edge:"right"});
    $('.collapsible').collapsible()
    $('.modal').modal();
    $('.parallax').parallax();
    $('#textarea1').val('');
  M.textareaAutoResize($('#textarea1'));
   $('select').formSelect();
  $('.datepicker').datepicker({
      format:"dd mmmm,yyyy",
      yearRange:3,
      showClearBtn:true,
      i18n:{
        done:"Select"
      }
  });
  });
  