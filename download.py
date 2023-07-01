import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    media_id = request.form.get('mediaId')

    # Construct the Instagram API URL
    url = f"https://www.instagram.com/reel/{media_id}"

    try:
        # Send a request to download the media
        response = requests.get(url, stream=True)

        if response.status_code == 200:
            # Extract the file extension from the response headers
            content_type = response.headers['content-type']
            extension = content_type.split('/')[-1]

            # Generate a filename for the downloaded media
            filename = f"{media_id}.{extension}"

            # Save the media file
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)

            return jsonify({'success': True, 'filename': filename})
        else:
            return jsonify({'success': False, 'error': 'Failed to download media'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run()
