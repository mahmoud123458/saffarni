document.getElementById('filterForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent the form from submitting normally

    // Get the form data
    let formData = new FormData(this);

    // Construct the URL with form data
    let url = this.action + '?' + new URLSearchParams(formData).toString();

    // Redirect to the filtered results page
    window.location.href = url;
});
