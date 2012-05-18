/* 
    Module: Router
    Handle all routing interactions with server by using Backbone. 

    Dependencies:
        $
        Backbone
*/
define(
    [
        "jQuery",
        "Backbone",
        "controller/loadTab",
    ], 
    function ($, Backbone, LoadTabController) {

        /*
            Class: NavRouter
            Handle all navigational routing actions by using Backbone.

            Subclasses:
                <Backbone.Router at http://documentcloud.github.com/backbone/#Router>

            Routes:
                /rankings - Load a Rankings page.
                /games - Load a Games list page.
        */
        var NavRouter = Backbone.Router.extend({

            routes: {
                ":tab":             "loadTab",     // load tab
                "*error":           "error"         // error catch all
            },

            loadTab: function (tab) {
                console.log("ajax load tab: " + tab);
                $.ajax({
                    type: "GET",
                    url: tab, 
                    data: {"asynch": true},
                    beforeSend: function () {
                        LoadTabController.handleSubmit();
                    },
                    success: function (jsonResponse) {
                        LoadTabController.handleSuccess(
                                jsonResponse.context_header,
                                jsonResponse.content
                        );
                    },
                });
            },

            error: function (error) {
                console.log("no handler: " + error);
            },
        });


        /*
            Function: initialize
            Initialize NavRouter's history and handle PushState

            Parameters:
                pushState - boolean turning pushState on or off. If 
                            true then remove default link functionality.
        */
        var initialize = function (pushState) {
        
            // Backbone using History API's PushState
            var appRouter = new NavRouter;
            var options = {silent: true};
            if (pushState) {
                options.pushState = true;
            }
            
            Backbone.history.start(options);

            return appRouter;
        }

        return {
            initializeAppRouter: initialize,
        };

    }
);
