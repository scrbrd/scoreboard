/**
    A set of function for DOM manipulations.

    @exports DOMUtil

    @requires $
*/
define(
        [
            "jQuery",
        ],
        function($) {

    /**
        Get id name from a id selector by stripping leading '#'.
        @param {string} idSelector A single id selector. 
        @return {string} The id value. 
    */
    function getIDFromSelector(idSelector) {
        return idSelector.substr(1); 
    }

        
    /**
        Get id selector from an id by adding a leading '#'.
        @param {string} id A single id. 
        @return {string} The id selector. 
    */
    function getSelectorFromID(id) {
        return "#" + id; 
    }


    /**
        Get class name from a class selector by stripping leading '.'.
        @param {string} classSelector A single class selector.
        @return {string} The class name. 
    */
    function getClassFromSelector(classSelector) {
        return classSelector.substr(1); 
    }

        
    /**
        Get class selector from an class by adding a leading '.'.
        @param {string} class A single class. 
        @return {string} The class selector. 
    */
    function getSelectorFromClass(className) {
        return "." + className; 
    }


    return { 
        getIDFromSelector: getIDFromSelector,
        getSelectorFromID: getSelectorFromID,
        getClassFromSelector: getClassFromSelector,
        getSelectorFromClass: getSelectorFromClass,
    };
});

