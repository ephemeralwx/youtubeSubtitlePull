'''
import re
import json
youtube_link = "(insert youtube video url/link here)"
video_id_match = re.search(r'v=([^&]+)', youtube_link)

if video_id_match:
    video_id = video_id_match.group(1)
    print(video_id)
else:
    print("Video ID not found in the URL.")


from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import Formatter

from youtube_transcript_api.formatters import JSONFormatter

# Must be a single transcript.
transcript = YouTubeTranscriptApi.get_transcript(video_id)
print("transcript received the youtube api vid link")
#print(transcript)

formatter = JSONFormatter()

 #.format_transcript(transcript) turns the transcript into a JSON string.
#json_formatted = formatter.format_transcript(transcript)
json_formatted = JSONFormatter().format_transcript(transcript, indent=2)


 #Now we can write it out to a file.
with open('captionsfull.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_formatted)



try:
    with open('captionsfull.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    text_values = [item['text'] for item in data]
    coherent_sentence = ' '.join(text_values)

    print(coherent_sentence)
except FileNotFoundError:
    print("File not found.")
except json.JSONDecodeError:
    print("JSON decoding error.")

 #Now should have a new JSON file that you can easily read back into Python.




'''
