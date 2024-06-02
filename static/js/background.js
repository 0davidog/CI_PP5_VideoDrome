/*jshint esversion: 6 */

window.addEventListener('DOMContentLoaded', () => {
    
    function updateBackgroundImage() {

        const bgElement = document.querySelector('#base-body');
    
        const mobileImageUrl = 'static/images/videodrome_bg_mobile.webp';
        const desktopImageUrl = 'static/images/videodrome_bg.webp';
    
        if (window.innerWidth <= 1200) { // You can adjust the width as per your requirement
            bgElement.style.backgroundImage = `url('${mobileImageUrl}')`;
        } else {
            bgElement.style.backgroundImage = `url('${desktopImageUrl}')`;
        }
        
    }
    

    // Initial check
    updateBackgroundImage();
    
    // Update on window resize
    window.addEventListener('resize', updateBackgroundImage);

});
