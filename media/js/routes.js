

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
            success: function(html) {
                update_content(html.content);
            }
        });
    },

    home: function() {
        console.log("no handler");
    }

});

// Updates the Context Content Tag with the new HTML
function update_content(html) {
    $('#content').html(html);

}

