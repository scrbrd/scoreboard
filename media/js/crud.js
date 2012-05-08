/* 
    Module: Crud
    Handle all Create, Read, Update, Delete actions on specific model objects.
    
    Dependencies:
        $ 
*/
define(
    [
        "jQuery",
    ],
    function($) {
        return {
            

            /*
                Constants: Request Keys
                XSRF - Used to indicate XSRF token
                ASYNCH - Used to indicate asynchronous request
                PARAMS - Used to indicate object parameters
            */
            KEY: {
                XSRF:       "_xsrf",
                ASYNCH:     "asynch",
                PARAMS:     "parameters",
            },


            /* 
                Constants: API Objects
                GAME - Corresponds to model.api.game.Game
            */
            OBJECT: {
                GAME:       "game",
            },


            /* 
                Function: createGame
                Create a new Game.
            
                Parameters:
                    parameters - the parameters that define this object
            */
            createGame: function(obj_params) {
                // TODO: make the obj_params more specific
                this._create(this.OBJECT.GAME, obj_params);
            },


            /* 
                Function: _create
                Create a new object.
            
                PRIVATE
                
                Parameters:
                    type - the object type to create
                    parameters - the parameters that define this object
            */
            _create: function(type, obj_params) {

                // move xsrf token to request parameters
                xsrf_token = obj_params[this.KEY.XSRF];
                delete obj_params[this.KEY.XSRF];

                escaped_params = JSON.stringify(obj_params);
                request_data = {};
                request_data[this.KEY.ASYNCH] = true; 
                request_data[this.KEY.XSRF] = xsrf_token;
                request_data[this.KEY.PARAMS] = escaped_params;
                
                $.post(
                    "/create/" + type, 
                    request_data, 
                    function(json_response) {
                        success = json_response.is_success;
                        console.log("success? " + json_response.is_success);
                        // TODO: if success or fail, tell user
                        if (success) {
                            // DocView.refresh();
                        }
                        // TODO: if success reload page
                    },
                    "json"
                );
            },
        };
    }
);

