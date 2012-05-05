/* Filename: crud.js
 *
 * Manage all Create, Read, Update, Delete actions.
 * A stand in for Model.
 *
 * global require
 *
 */

define(
    [
        // Aliases from main.js to module versions of packages
        "jQuery",
    ],
    function($) {

        // Router for any ajax object requests.
        var CrudHandler = {
            
            // send new object to server
            create: function(type, parameters) {
                // move _xsrf to highest level parameter
                _xsrf = parameters["_xsrf"];
                delete parameters["_xsrf"];

                escaped_params = JSON.stringify(parameters);
                data = {
                    "asynch": true, 
                    "_xsrf": _xsrf,
                    "parameters": escaped_params,
                    };
                $.post(
                        "/create/" + type, 
                        data, 
                        function(json) {
                            console.log("success? " + json.is_success);
                        },
                        "json");
            },
        };

        return CrudHandler;
    }
);

