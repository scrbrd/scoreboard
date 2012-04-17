

var AppRouter = Backbone.Router.extend({

    routes: {
        ":tab":     "load_tab", // new tab
        "*error":         "error"      // error catch all
    },

    load_tab: function(tab) {
        console.log("ajax load tab: " + tab);
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

    error: function(error) {
        console.log("no handler: " + error);
    }

});


