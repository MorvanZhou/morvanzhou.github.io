
$(function () {

  var msie6 = $.browser == 'msie' && $.browser.version < 7;

  if (!msie6 && $('.tut-right-bar').offset()!=null) {
    var top = $('.tut-right-bar').offset().top - parseFloat($('.tut-right-bar').css('margin-top').replace(/auto/, 0));
    var height = Math.max(1100, $('.tut-right-bar').height());
    var winHeight = $(window).height();
    var footerTop = $('footer').offset().top + 20 - parseFloat($('footer').css('margin-top').replace(/auto/, 0));
    var gap = 4;
    $(window).scroll(function (event) {
      // what the y position of the scroll is
      var y = $(this).scrollTop();

      // whether that's below the form
      if (y + winHeight >= top + height + gap && y + winHeight <= footerTop) {
        // if so, ad the fixed class
        $('.tut-right-bar').addClass('tut-right-bar-fixed').css('top', winHeight - height - gap +'px');
      }
      else if (y + winHeight > footerTop) {
        // if so, ad the fixed class
       $('.tut-right-bar').addClass('tut-right-bar-fixed').css('top', footerTop - height - y - gap+'px');
      }
      else
      {
        // otherwise remove it
        $('.tut-right-bar').removeClass('tut-right-bar-fixed').css('top','0px');
      }
    });
  }
});
