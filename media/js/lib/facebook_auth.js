/* Module: facebook_auth
 *
 * Facebook Authentication for Login
 *
 * NOTE: Currently unused
 * TODO Remove
 *
 */

//initialize facebook connection and check login status
window.fbAsyncInit = function() {
    console.log('fbAsyncInit');

    FB.init({
        appId       : '184725354981659', // App ID
        status      : true, // check login status
        cookie      : true, // enable cookies to allow the server to access the session
        xfbml       : true,  // parse XFBML
        channelUrl  : "//hammer.sqoreboard.com/static/channel.html"
    });

    // Check if use is logged in
    FB.getLoginStatus(function(response) {
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
};

// Load the SDK Asynchronously
(function(d){
    console.log('SDK load function');
    var js, id = 'facebook-jssdk'; 
    if (d.getElementById(id)) {
        return;
    }
    js = d.createElement('script'); 
    js.id = id;
    js.async = true;
    js.src = "//connect.beta.facebook.net/en_US/all.js";
    d.getElementsByTagName('head')[0].appendChild(js);
    console.log('here');
}(document));

//login User
function loginUser() {    
    FB.login(function(response) { },
        {scope:'email,user_interests'});     
}
 
