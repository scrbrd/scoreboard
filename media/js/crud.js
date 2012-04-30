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

        return CrudHandler;
    }
);

