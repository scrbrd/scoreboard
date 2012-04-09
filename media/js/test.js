/* global _, $, Backbone */

$.ajaxSetup({
    cache: false
});

var app_router = new App;
Backbone.history.start();
