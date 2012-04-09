var myScrolls = [];

var myScroll = function () {
    var scroller_id = 'wrapper';

    if (scroller_id in myScroll) {
        myScrolls[scroller_id].refresh();
    } else {
        myScrolls[scroller_id] = new iScroll(
                scroller_id,
                {
                    hScroll         : false,
                    vScroll         : true,
                    hScrollbar      : false,
                    vScrollbar      : true,
                    fixedScrollbar  : true,
                    fadeScrollbar   : false,
                    hideScrollbar   : false,
                    bounce          : true,
                    momentum        : true,
                    lockDirection   : false
                });
    }
};

$(document).delegate('[data-role="page"]', 'pageshow', myScroll);
$(document).delegate('[data-role="page"]', 'pagecreate', myScroll);
$(window).bind('orientationchange', myScroll);

//document.body.addEventListener(
//    'touchmove',
//    function(e) {
//        e.preventDefault();
//    },
//    false);
