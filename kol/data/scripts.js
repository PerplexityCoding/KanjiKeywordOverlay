(function ($) {

    $('.kol-kanji').off('mouseenter').on('mouseenter', (e) => {
        const $parent = $(e.currentTarget).closest('.kol');
        const $overlay = $parent.find('.kol-overlay');
        const windowWidth = $('body').outerWidth(true);
        const overflowDiff = windowWidth - ($parent.offset().left + $overlay.outerWidth(true));
        const $parentOffset = $parent.offset();

        let left = $parentOffset.left;
        if (overflowDiff < 0) {
            left += overflowDiff - 5;
        }

        $overlay.css({
            top: $parentOffset.top + $parent.outerHeight(true) + 5,
            left: left + 'px',
            visibility: 'visible'
        });
    });

    $('.kol-kanji').off('mouseleave').on('mouseleave', (e) => {
        const $parent = $(e.currentTarget).closest('.kol');
        const $overlay = $parent.find('.kol-overlay');
        $overlay.css({
            visibility: 'hidden'
        });
    });

})(window.$);

