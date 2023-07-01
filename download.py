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
        # Add your logic here to save the media file

        return jsonify({'success': True})
    except:
        return jsonify({'success': False})

if __name__ == '__main__':
    app.run()
