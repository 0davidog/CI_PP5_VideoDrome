/*jshint esversion: 6 */
/* globals bootstrap */

/* Source: https://getbootstrap.com/docs/5.3/components/toasts/
Reveals Bootstrap toast message */

window.addEventListener('DOMContentLoaded', () => {

    const messageToast = document.getElementById('message-toast');
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(messageToast);

    toastBootstrap.show();

});