window.addEventListener('DOMContentLoaded', () => {
    const userRating = parseInt(document.getElementById('user-rating').innerHTML);
    const starRatings = document.getElementsByClassName('star-rating');

    for (let i = 1; i <= 5; i++) {
        let star = document.getElementById(`star-${i}`);
        if (userRating >= i) {
            star.classList.remove('fa-regular');
            star.classList.add('fa-solid');
        } else {
            star.classList.remove('fa-solid');
            star.classList.add('fa-regular');
            star.onmouseover = function() {
                star.classList.remove('fa-regular');
                star.classList.add('fa-solid');
            }
            star.onmouseout = function() {
                star.classList.remove('fa-solid');
                star.classList.add('fa-regular');
            }
        }
    }

});
