/* Header Scroll */
$(window).scroll(function () {
    if ($(window).scrollTop() > 20) {
        $('.header-main').addClass('fixed-header');
    } else {
        $('.header-main').removeClass('fixed-header');
    }
});