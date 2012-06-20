/**
    @namespace
    @name util
*/
define(
        [
            "jQuery",
            "js/constants",
        ],
        /**
            A utility for generic DOM manipulations.

            @exports DOM

            @requires $
            @requires Const
        */
        function($, Const) {

        
    /**
        Get id name from a id selector by stripping leading '#'.
        @param {string} idSelector A single id selector. 
        @return {string} The id value. 
    */
    function getIDFromIDSelector(idSelector) {
        return idSelector.substr(1); 
    }


    /**
        Get class name from a class selector by stripping leading '.'.
        @param {string} classSelector A single class selector.
        @return {string} The class name. 
    */
    function getClassFromClassSelector(classSelector) {
        return classSelector.substr(1); 
    }

    return /** @lends module:util.Dom */ {
        getIDFromIDSelector: getIDFromIDSelector,
        getClassFromClassSelector: getClassFromClassSelector,
    };
});

