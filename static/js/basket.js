// This block of code handles the click event for elements with the class 'update-link'
$('.update-link').click(function(e) {
    // Find the form element that comes before the clicked element with the class 'update-link'
    let form = $(this).prev('.update-form');
    // Submit the form
    form.submit();
});