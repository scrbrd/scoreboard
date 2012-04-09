

var App = Backbone.Router.extend({

    routes: {
        "test2":    "test2"     // #test2
    },

    test2: function() {
        console.log("clicked on test2");
        $.ajax({
            type: "GET",
            url: "test2",
        }).done(function(html) {
            $('#scroller').html(html);
        });
    }
});

console.log("App defined");
