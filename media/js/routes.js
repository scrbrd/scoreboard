

var App = Backbone.Router.extend({

    routes: {
        ":tab":     "load_tab",     // new tab
        "":    "home"
    },

    load_tab: function(tab) {
        console.log("clicked on tab");
        $.ajax({
            type: "GET",
            url: "a/" + tab,
            success: function(html) {
                update_context_content(html);
            }
        });
    },

    home: function() {
        console.log("no handler");
    }

});

// Updates the Context Content Tag with the new HTML
function update_context_content(html) {
    $('#iscroll_wrapper').html(html);

}

