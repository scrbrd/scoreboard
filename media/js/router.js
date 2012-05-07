/* Filename: router.js
 *
 * Router wraps Backbone Routes
 *
 * global require
 *
 */

define(
    [
        "jQuery",
        "Backbone",
        "view/document",
    ], 
    function($, Backbone, DocView) {

        // Router for any page requests (usually affects URL/history) -
        // Backbone
        var NavRouter = Backbone.Router.extend({

            routes: {
                ":tab":             "loadTab",     // load tab
                "*error":           "error"         // error catch all
            },

            loadTab: function(tab) {
                console.log("ajax load tab: " + tab);
                $.ajax({
                    type: "GET",
                    url: tab, 
                    data: {"asynch": true},
                    beforeSend: function() {
                        DocView.getDocumentView().hideContent();
                    },
                    success: function(json_response) {
                        doc_view = DocView.getDocumentView();
                        doc_view.updateContent(json_response.content);
                        doc_view.updateContext(json_response.context_header);
                    }
                });
            },

            error: function(error) {
                console.log("no handler: " + error);
            },

        });

        // Set up Backbone's Router
        var initialize = function(pushState) {
        
            // Backbone using History API's PushState
            var app_router = new NavRouter;
            if (pushState) {
                Backbone.history.start({
                    pushState: true,
                    silent: true
                });
            
                // SRC = https://github.com/tbranyen/backbone-boilerplate
                // All navigation that is relative should be passed through the navigate
                // method, to be processed by the router.  If the link has a data-bypass
                // attribute, bypass the delegation completely.
                $(document).on("click", "a:not(.data-bypass)", function(event) {
                    // Get the anchor href and protcol
                    var href = $(this).attr("href");
                    var protocol = this.protocol + "//";

                    // Ensure the protocol is not part of URL, meaning its relative.
                    if (href && href.slice(0, protocol.length) !== protocol) {
                
                        // Stop the default event to ensure the link will not cause a page
                        // refresh.
                        event.preventDefault();

                        // `Backbone.history.navigate` is sufficient for all Routers and will
                        // trigger the correct events.  The Router's internal `navigate` method
                        // calls this anyways.
                        if (!$(this).hasClass('route-bypass')) {
                            app_router.navigate(href, {trigger: true});
                        }
                    }
                });
            
            // Backbone without using History's PushState
            } else {
                Backbone.history.start({
                        silent: true
                });
            } 
        }

        // Return a Router object with functions
        return {
            initialize: initialize, // associates NavRouter with Backbone
        }

    }
);
