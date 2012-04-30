/* Filename: underscore.js
 *
 * Wrapper around underscore to modularize it.
 *
 * global require, _,
 *
 */

define(["order!libs/underscore/underscore-min"], function() {
    // Tell Require.js that this module returns a reference to Underscore.
    return _;
});

