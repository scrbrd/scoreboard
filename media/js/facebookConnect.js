// Facebook Authentication for Login
// Evan Hammer
// 2012.01.17

//initialize facebook connection and check login status
window.fbAsyncInit = function() {
    FB.init({
        appId      : '292549250794068', // App ID
        status     : true, // check login status
        cookie     : true, // enable cookies to allow the server to access the session
        xfbml      : true  // parse XFBML
    });

    // Check if use is logged in
    FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
            // the user is logged in and connected to your
            // app, and response.authResponse supplies
            // the user's ID, a valid access token, a signed
            // request, and the time the access token 
            // and signed request each expire
            var uid = response.authResponse.userID;
            var accessToken = response.authResponse.accessToken;
            alert('user logged in: ' + uid);
        } else if (response.status === 'not_authorized') {
            // the user is logged in to Facebook, 
            // but not connected to the app
            alert('user logged in but not connected to app');
        } else {
            // the user isn't even logged in to Facebook.
            alert('user not logged into facebook');
        }
    });
};

// Load the SDK Asynchronously
(function(d){
    alert('SDK load function');
    var js, id = 'facebook-jssdk'; 
    if (d.getElementById(id)) {return;}
    js = d.createElement('script'); js.id = id;
    js.async = true;
    js.src = "//connect.facebook.net/en_US/all.js";
    d.getElementsByTagName('head')[0].appendChild(js);
}(document));

//login User
function loginUser() {    
    FB.login(function(response) { },
        {scope:'email,user_interests'});     
}
 
