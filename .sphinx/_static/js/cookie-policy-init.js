import { cookiePolicy } from '@canonical/cookie-policy';
// npx webpack --config webpack.config.js terminal to bundle policy 

const getCookie = (targetCookie) => {
    document.cookie.match(new RegExp("(^| )" + targetCookie + "=([^;]+)"));
}
let cookieAcceptanceValue = getCookie("_cookies_accepted");

if (!cookieAcceptanceValue) {
    cookiePolicy(setUserId);
} else {
    setUserId();
    cookiePolicy();
}

function setUserId() {
    cookieAcceptanceValue = getCookie("_cookies_accepted");
    if (
      cookieAcceptanceValue?.[2] === "all" ||
      cookieAcceptanceValue?.[2] === "performance"
    ) {
      // Check if user doesn't already have a user_id
      if (!getCookie("user_id")) {
        // Generate a universally unique identifier
        const user_id = generateUUID();
        document.cookie = "user_id=" + user_id + ";max-age=31536000;";

        dataLayer.push({
          user_id: user_id,
        });
      }
    }
}
function generateUUID() {
      return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
        (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
      );
}