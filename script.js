document.getElementById('downloadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var url = document.getElementById('instagramURL').value;

    // Validate URL
    if (url.includes('instagram.com')) {
        // Remove any trailing slash from the URL
        url = url.replace(/\/$/, '');

        // Extract the media ID from the URL
        var mediaId = url.substr(url.lastIndexOf('/') + 1);

        // Send a request to the server to download the media
        downloadMedia(mediaId);
    } else {
        displayErrorMessage('Invalid Instagram URL');
    }
});

function downloadMedia(mediaId) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);

            if (response.success) {
                displaySuccessMessage('Download completed');
            } else {
                displayErrorMessage('Download failed');
            }
        }
    };

    xhr.open('POST', 'download.php', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send('mediaId=' + encodeURIComponent(mediaId));
}

function displayErrorMessage(message) {
    var results = document.getElementById('results');
    results.innerHTML = '<p class="error">' + message + '</p>';
}

function displaySuccessMessage(message) {
    var results = document.getElementById('results');
    results.innerHTML = '<p class="success">' + message + '</p>';
}
