/* Filename: backbone.js
 *
 * Wrapper around backbone to modularize it.
 *
 * global require, $, _, Backbone
 *
 */

define(["order!libs/backbone/backbone-min"], function() {
    // Call noConflct to remove globals
    _.noConflict();
    $.noConflict();
    return Backbone.noConflict();
});
