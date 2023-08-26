from flask import Flask, request, jsonify
import re
import json
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
import requests
app = Flask(__name__)
#url = "http://127.0.0.1:5000/get_subtitles"
#data = {
#    "youtube_link": "https://www.youtube.com/watch?v=cCzrJjn7p7U"
#}
@app.route('/get_subtitles', methods=['GET'])
def get_subtitles():


    youtube_link = request.args.get('youtube_link', '')

    video_id_match = re.search(r'v=([^&]+)', youtube_link)
    if not video_id_match:
        return jsonify({"error": "Video ID not found in the URL."}), 400

    video_id = video_id_match.group(1)

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        return jsonify({"error": f"Failed to fetch transcript: {str(e)}"}), 500

    json_formatted = JSONFormatter().format_transcript(transcript, indent=2)

    data = json.loads(json_formatted)
    text_values = [item['text'] for item in data]
    coherent_sentence = ' '.join(text_values)

    #print("the following is printed:")
    #print(jsonify({"subtitles": coherent_sentence}), 200)
    #print("the following is returned:")
    return jsonify({"subtitles": coherent_sentence}), 200
    
if __name__ == '__main__':
    app.run(debug=True)
