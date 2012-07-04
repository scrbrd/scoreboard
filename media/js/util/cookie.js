/**
    A set of functions for manipulating cookies.

    See: http://www.quirksmode.org/js/cookies.html

    @exports CookieUtil
*/
define(
        [
        ],
        function () {


/**
    Create a new cookie.
    @param {string} name
    @param {string} value
    @param {number} days days until the cookie should expire.
*/
function createCookie(name,value,days) {
    var date;
    var expires = "";
    if (days) {
        date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    }
    document.cookie = name + "=" + value + expires + "; path=/";
}

/**
    Read an existing cookie.
    @param {string} name
*/
function readCookie(name) {
    var nameEQ = name + '=';
    var ca = document.cookie.split(';');
    for(var i = 0;i < ca.length; i += 1) {
        var c = ca[i];
        while (c.charAt(0) === ' ') {
            c = c.substring(1, c.length);
        }
        if (c.indexOf(nameEQ) === 0) {
            return c.substring(nameEQ.length,c.length);
        }
    }
    return null;
}

/**
    Erase cookie.
    @param {string} name
*/
function eraseCookie(name) {
    createCookie(name, "", -1);
}

return {
    createCookie: createCookie,
    readCookie: readCookie,
    eraseCookie: eraseCookie,
    checkCookie: function (name) {
        if (readCookie(name) === null) {
            return false;
        } else {
            return true;
        }
    }
};


});
