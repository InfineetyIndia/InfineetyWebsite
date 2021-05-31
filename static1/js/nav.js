/*
 * Responsive Navigation Menu v4.1.1
 * https://webgadgets.net/plugins/responsive-navigation-menu
 *
 * Copyright 2016, WebGadgets
 * Free to use and abuse under the MIT license.
 * http://www.opensource.org/licenses/mit-license.php
 *
 * Date: 2017-05-27
 */
(function ($) {
    $.fn.responsiveNav = function (options) {

        // Establish our default settings
        var settings = $.extend({
            type: 'horizontal', //vertical, horizontal
            offCanvas: false,
            openSubmenuOnClick: false,
            openSubmenuOnHover: true,
            activateOnWidth: 0,
            theme: 'light',
            menuIcon: true
        }, options);

        return this.each(function () {
            var rn = $(this);
            var rn_class;
            if (settings.activateOnWidth > 0) {
                rn_class = 'responsive-nav-cr';
            } else {
                rn_class = 'responsive-nav';
            }


            rn.addClass(rn_class);

            $("." + rn_class + " li.dropdown > a").on("click", function () {
                if (viewport().width < 768 || (viewport().width < settings.activateOnWidth)) {
                    return false;
                }
            });

            rn.find("li.dropdown a").on("click", function () {
                if (viewport().width < 768 || (viewport().width < settings.activateOnWidth)) {
                    $(this).parent('li.dropdown').siblings('li.dropdown').removeClass('open');
                    $(this).parent('li.dropdown').toggleClass('open', 300);
                    $(this).parent('li.dropdown').children('div').children('ul').children('li.dropdown').removeClass('open');
                }
            });

            rn.children("." + rn_class + " .label-menu").on("click", function () {
                if (viewport().width < 768 || (viewport().width < settings.activateOnWidth)) {
                    $(this).next('div').children('ul').children('li.dropdown').removeClass('open');
                    $(this).next('div').toggleClass('first-open', 300);
                }
            });

            if (settings.menuIcon === true) {
                rn.children('.label-menu').append('<span class="menu-icon"></span>');
            }
            if (settings.offCanvas === true) {
                rn.addClass('off-canvas');
                //off canvas menu
                rn.children("." + rn_class + ".off-canvas .label-menu").on("click", function () {
                    if (viewport().width < 768 || (viewport().width < settings.activateOnWidth)) {
                        $(this).next('div').toggleClass('first-open-oc', 300);
                        $(".bg-canvas").remove();
                        $(this).next('div').after("<div class=\"bg-canvas\"></div>");
                    }
                });
                $(document).on("click", ".bg-canvas", function () {
                    $(this).prev('div').removeClass('first-open-oc');
                    $(this).prev('div').removeClass('first-open');
                });
                rn.children('div').children('ul').prepend('<li class="close-menu"><a href="javascript:void(0);" onclick="$(\'.bg-canvas\').trigger(\'click\');"><span></span></a></li>');
            }

            if (settings.type === 'vertical') {
                rn.addClass(settings.type);
            }

            if (settings.activateOnWidth > 0) {
                $(window).on("load resize", function (e) {
                    if (viewport().width < settings.activateOnWidth) {
                        rn.addClass('responsive-nav-activate');
                    } else {
                        rn.removeClass('responsive-nav-activate');
                    }
                });
            }

            if (settings.openSubmenuOnHover === false) {
                rn.addClass('disableHoverDD');
            }
            if (settings.openSubmenuOnClick === true) {
                $('html').click(function () {
                    //Hide the menus if visible
                    $('.dropdown.open-click').removeClass('open-click');
                });
//                $("." + rn_class + " > div > ul > .dropdown").click(function (event) {
                $("." + rn_class + " > div > ul .dropdown a").click(function (event) {
                    event.stopPropagation();
                });
//                rn.find('div > ul > li.dropdown > a').click(function () {
                rn.find('div > ul > li.dropdown > a').click(function () {
                    $(this).parent('.dropdown').siblings('.open-click').find('.open-click').removeClass('open-click');
                    //$(this).siblings('.open-click').find('.open-click').removeClass('open-click');
                });
                rn.find('div > ul > li.dropdown a').click(function () {
                    if (viewport().width >= 768 || (settings.activateOnWidth > 0 && viewport().width >= settings.activateOnWidth)) {
                        $(this).parent('.dropdown').siblings('.open-click').removeClass('open-click');
                        $(this).parent('.dropdown').toggleClass('open-click');
                        //$(this).parent('.dropdown').parents('.dropdown').toggleClass('open-click');
                    }
                });
            }

            if (settings.theme !== '') {
                rn.addClass(settings.theme);
            }

        });
    };

    function viewport() {
        var e = window, a = 'inner';
        if (!('innerWidth' in window)) {
            a = 'client';
            e = document.documentElement || document.body;
        }
        return {width: e[ a + 'Width' ], height: e[ a + 'Height' ]};
    }
}(jQuery));
