/**
    Wrapper around backbone to modularize it.
*/
define(["order!lib/backbone/backbone-min"], function() {
    // Call noConflct to remove globals
    // TODO make undercore a real module using:
    // https://github.com/dzejkej/modular-backbone
    //_.noConflict();
    $.noConflict();
    return Backbone.noConflict();
});
