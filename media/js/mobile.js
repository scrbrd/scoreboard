
var theScroll;
var myScroll;

$(document).ready(function loaded() {
    myScroll = new iScroll('wrapper');
    document.addEventListener('touchmove', function (e) { e.preventDefault(); }, false);
    document.addEventListener('DOMContentLoaded', function () { setTimeout(loaded, 200); }, false);
});
