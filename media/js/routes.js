// Module: routes
//
// Both Backbone routes and Standalone routes

// Router for any page requests (usually affects URL/history)
var NavRouter = Backbone.Router.extend({

    routes: {
        ":tab":             "load_tab",     // load tab
        "*error":           "error"         // error catch all
    },


    load_tab: function(tab) {
        console.log("ajax load tab: " + tab);
        $.ajax({
            type: "GET",
            url: tab, 
            data: {"asynch": true},
            beforeSend: function() {
                DomManager.hide_content();
            },
            success: function(json_response) {
                DomManager.update_content(json_response.content);
                DomManager.update_context(json_response.context_header);
            }
        });
    },

    error: function(error) {
        console.log("no handler: " + error);
    }

});

// Router for any ajax object requests.
var CrudRouter = {
    
    // send new object to server
    create: function(type, parameters) {
        escaped_params = JSON.stringify(parameters);
        data = {"asynch": true, "parameters": escaped_params};
        $.post(
                "/create/" + type, 
                data, 
                function(json) {
                    console.log(json);
                },
                "json");
    },



};

