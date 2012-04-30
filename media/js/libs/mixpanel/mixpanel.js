/* Filename: mixpanel.js
 *
 * Wrapper around mixpanel
 * Version 2?
 *
 * global require
 *
 */

define(function() {

    // Code pulled from MixPanel Documentation
    (function(d,c){var a,b,g,e;a=d.createElement("script");a.type="text/javascript";
    a.async=!0;a.src=("https:"===d.location.protocol?"https:":"http:")+
    '//api.mixpanel.com/site_media/js/api/mixpanel.2.js';b=d.getElementsByTagName("script")[0];
    b.parentNode.insertBefore(a,b);c._i=[];c.init=function(a,d,f){var b=c;
    "undefined"!==typeof f?b=c[f]=[]:f="mixpanel";g=['disable','track','track_pageview',
    'track_links','track_forms','register','register_once','unregister','identify',
    'name_tag','set_config'];
    for(e=0;e<g.length;e++)(function(a){b[a]=function(){b.push([a].concat(
    Array.prototype.slice.call(arguments,0)))}})(g[e]);c._i.push([a,d,f])};window.mixpanel=c}
    )(document,[]);

    // Sqoreboard Token from MixPanel Dashboard
    mixpanel.init("21e3cfefb46bbded0d61eb0dca4bcec7");

    // Tell Require.js that this module returns a reference to mixpanel.
    return mixpanel;
});

