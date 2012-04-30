/* Filename: jquery.js
 *
 * Wrapper around jquery to modularize it.
 *
 * global require, $,
 *
 */

define(["order!libs/jquery/jquery-min"], function() {
    // Tell Require.js that this module returns a reference to jQuery.
    return $;
});
