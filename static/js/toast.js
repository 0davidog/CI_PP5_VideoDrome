/* Source: https://getbootstrap.com/docs/5.3/components/toasts/
Reveals Bootstrap toast message */

const messageToast = document.getElementById('message-toast');
const toastBootstrap = bootstrap.Toast.getOrCreateInstance(messageToast);
toastBootstrap.show()
