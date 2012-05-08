/* Filename: jquery.js
 *
 * Wrapper around jquery to modularize it.
 *
 * global require, $,
 *
 */

define([
        "order!lib/jquery/jquery-min",
        "order!lib/jquery/jquery-ui/jquery-ui-min",
        "order!lib/jquery/form2js/form2js",
        "order!lib/jquery/form2js/jquery.toObject",
        ], function() {
    // Tell Require.js that this module returns a reference to jQuery.
    return $;
});
