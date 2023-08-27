'''
Script to download the youtube video (audio). Note that this script is
really a Flask server 

1. Recieves a POST request from the extension upon UI interaction,
url recieved as a string

2. Using the youtube_dl package, executes the download of the youtube
video audio, as an mp3 (?) (UPDATE: m4a)

3. Sends a response to the extension upon download completion, logs to
the browser console (Still gotta work on this one, but optional)
'''

from __future__ import unicode_literals
import yt_dlp
from flask import Flask, request, make_response
import json

app = Flask(__name__)

# Code to (hopefully) log yt_dlp's progress in the console
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

@app.route('/YTMusic.py', methods = ['POST'])
def init_download():
    # Execute download here
    print("Request received...")
    page_url = json.loads(request.data)['video_url'].strip()
    print('The url is ' + page_url)
    response = make_response('Download initiated', 200)
    response.mimetype = "text/plain"

    # Set to download audio only
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'ffmpeg_location': '/Users/jeffmassman/Desktop/YTMusic/ffmpeg',
        'writethumbnail': True,
        'embedthumbnail': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': 'best',
        },
        {
            'key': 'EmbedThumbnail',
        }],
        'outtmpl': '/Users/jeffmassman/Music/iTunes/iTunes Media/Automatically Add to Music.localized/%(title)s' + '.m4a',
        'logger': MyLogger()
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([page_url])
    print("Request processed successfully!")
    return response

# 'outtmpl': '/Users/jeffmassman/Desktop/YTMusic/Songs/%(title)s' + '.m4a',

if __name__ == '__main__':
    print("Server now running...")
    app.run(port = 8080)