/*jshint esversion: 6 */
//Script to render stars in relation to user ratings on videos:

/**
* Script to render star icons in relation to user ratings on videos.
* Loads DOM content first.
 */

window.addEventListener('DOMContentLoaded', () => {
    const userRating = parseInt(document.getElementById('user-rating').innerHTML);

    const starRatings = document.getElementsByClassName('star-rating');

    for (let i = 0; i < starRatings.length; i++) {
        const rating = starRatings[i];
        const ratingNum = parseInt(rating.getAttribute('data-rating'));
        let starsHTML = '';
    
        for (let k = 1; k <= 5; k++) {
            if (k <= ratingNum) {
                starsHTML += `<i class="fa-solid fa-star"></i>`;
            } else {
                starsHTML += `<i class="fa-regular fa-star"></i>`;
            }
        }
    
        rating.innerHTML = starsHTML;
    }
    

    for (let j = 1; j <= 5; j++) {
        let star = document.getElementById(`star-${j}`);
        if (userRating >= j) {
            star.classList.remove('fa-regular');
            star.classList.add('fa-solid');
        } else {
            star.classList.remove('fa-solid');
            star.classList.add('fa-regular');
            star.onmouseover = function() {
                star.classList.remove('fa-regular');
                star.classList.add('fa-solid');
            };
            star.onmouseout = function() {
                star.classList.remove('fa-solid');
                star.classList.add('fa-regular');
            };
        }
    }

    

    

});
