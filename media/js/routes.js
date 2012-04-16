

var AppRouter = Backbone.Router.extend({

    routes: {
        ":tab":     "load_tab", // new tab
        "*splat":         "home"      // catch all
    },

    load_tab: function(tab) {
        $.ajax({
            type: "GET",
            url: tab, 
            data: "asynch=True", // FIXME make this valueless
            beforeSend: function() {
                hide_content();
            },
            success: function(html) {
                update_content_with_iscroll(html.content);
            }
        });
    },

    home: function() {
        console.log("no handler");
    }

});






