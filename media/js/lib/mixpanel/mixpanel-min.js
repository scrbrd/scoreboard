// Code pulled from MixPanel Documentation
(function(c,a){var b,d,h,e;b=c.createElement("script");b.type="text/javascript";
b.async=!0;b.src=("https:"===c.location.protocol?"https:":"http:")+
'//api.mixpanel.com/site_media/js/api/mixpanel.2.js';d=c.getElementsByTagName("script")[0];
d.parentNode.insertBefore(b,d);a._i=[];a.init=function(b,c,f){function d(a,b){
var c=b.split(".");2==c.length&&(a=a[c[0]],b=c[1]);a[b]=function(){a.push([b].concat(
Array.prototype.slice.call(arguments,0)))}}var g=a;"undefined"!==typeof f?g=a[f]=[]:
f="mixpanel";g.people=g.people||[];h=['disable','track','track_pageview','track_links',
'track_forms','register','register_once','unregister','identify','name_tag',
'set_config','people.set','people.increment'];for(e=0;e<h.length;e++)d(g,h[e]);
a._i.push([b,c,f])};a.__SV=1.1;window.mixpanel=a})(document,window.mixpanel||[]);
