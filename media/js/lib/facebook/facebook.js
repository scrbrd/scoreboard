/**
    Connects to the Facebook API and defines how application interacts with
    facebook.

    Note: We are currently doing authentication on both the client and the server.
    This is silly. When we no longer use the facebook widgets, we should remove
    client side authentication.

    @exports Facebook

 */
define(
        [],
        function () {


var APP_ID = '422553881116676';


//initialize facebook connection and check login status
window.fbAsyncInit = function () {
    console.log('fbAsyncInit');


    FB.init({
        appId: APP_ID, // App ID
        status: true, // check login status
        cookie: true, // enable cookies to allow the server to access the session
        xfbml: true,  // parse XFBML
        level: "debug",
        trace: true,
        autoRun: true
        // TODO: in prodcution include a channelURL
        //channelUrl: "//192.168.1.7:5000/static/channel.html"
    });

    // Check if use is logged in
    FB.getLoginStatus(function (response) {
        console.log("getLoginStatus");
        if (response.status === 'connected') {
            // the user is logged in and connected to your
            // app, and response.authResponse supplies
            // the user's ID, a valid access token, a signed
            // request, and the time the access token
            // and signed request each expire
            var uid = response.authResponse.userID;
            var accessToken = response.authResponse.accessToken;
            var expiresIn = response.authResponse.expiresIn;
            var signedRequest = response.authResponse.signedRequest;

            console.log('user logged in: ' + uid);
            console.log('accessToken: ' + accessToken);
            console.log('expiresIn: ' + expiresIn);
            console.log('signedRequest: ' +  signedRequest);
        } else if (response.status === 'not_authorized') {
            // the user is logged in to Facebook,
            // but not connected to the app
            console.log('user logged in but not connected to app');
        } else {
            // the user isn't even logged in to Facebook.
            console.log('user not logged into facebook');
        }
    });

    // Parse to setup HTML5 / XFBML plugins (including comments.)
    // FB.XFBML.parse();
};

// Load the SDK Asynchronously
(function (d, s, id) {
    console.log('SDK load function');
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {
        return;
    }
    js = d.createElement(s);
    js.id = id;
    js.src = "//connect.facebook.net/en_US/all.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

return {
    //login User
    loginUser: function () {
        console.log("Facebook logging in...");
        FB.login(
                function(response) {},
                {scope: 'email,user_interests'});
    }
};


});
