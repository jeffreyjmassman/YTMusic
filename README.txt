YTMusic is an extension I created to download music from YouTube
with the eventual goal to listen to it offline. The motivation is that
a lot of the music I listen to is only available on YouTube; however, to
listen to it (especially while running), I have to use up a lot of LTE.
Also, there are ads, and the music is unstable in the sense that it can
be deleted off youtube at any time; it has already happened to some of 
my songs. It is for these reasons I developed this project.

SETUP INSTRUCTIONS

1. If not already available, download and install FireFox
2. Download and install ffmpeg (https://evermeet.cx/ffmpeg/) 
    place into YTMusic folder
3. Install and/or update to Python 3
4. Make sure pip is installed (Open up Mac terminal and type:
    'python3 -m pip --version')
5. Install Flask : Type in terminal 'python3 -m pip install flask'
6. Install yt-dlp: Type in terminal 'python3 -m pip install yt-dlp'
7. Install VSCode (recommended) or any other text editor
8. Open up YTMusic using VSCode / text editor
9. Make the following changes:
    -manifest.json line 12: Change 'jeffmassman' to your Mac user name
    -YTMusic.py line 45: Change 'jeffmassman' to your Mac user name
    -YTMusic.py line 56: Change 'jeffmassman' to your Mac user name

INSTRUCTIONS - HOW TO USE

1. Open FireFox, and in the top search bar, type in 'about:debugging'
    - Note: This step needs to be done every time you restart your computer
2. On the page, on the left, click on 'This FireFox'
3. Click button that says 'Load Temporary Add-On...'
4. Find YTMusic and click on any folder within; the extension is now active
5. Open the Mac terminal
6. Type 'python3 /Users/YOURUSERNAME/Desktop/YTMusic/YTMusic.py'
    (Obviously, replace YOURUSERNAME with your Mac username lol)
7. Everything is ready! Navigate to any Youtube video whose audio you wish
    to download, and click the 'Download' button underneath the video,
    next to the 'Subscribe' button; the audio will automatically be added
    to your Apple Music song library
8. To shutdown the server, go to the terminal and press Ctrl + C
9. To get music on your phone, plug it in to your laptop, go to Apple
    Music, and click on your phone off to the left; click on sync settings
    and then go to Music; then sync the music as desired (Note: you may
    have to disable cloud music sharing for this to work; this may remove
    songs on your phone that are being shared using this feature; proceed
    at your own risk!)

NOTES / WARNINGS

- Do NOT refresh the page when on a YouTube video; the 'Download' button
    will disappear; bug still needs to be fixed
- Sometimes, the thumbnail will not load in; this is rare but watch
    carefully; if this happens, delete the song and reload
- If there is an error with requests reaching the server, this may be
    an issue with your firewall; disable it in settings
- For this code to work, the YTMusic folder must sit in your Desktop;
    otherwise, the file paths will need to be changed

CHANGELOG

What has been done so far (as of 7/10/23):

1. A basic UI has been set up on the front end via a javascript Firefox
    extension that adds a 'Download' button to YouTube
2. The button is designed to send a POST request of the current video URL 
to a server running on my MacBook
3. Said server was developed and setup using a simple web framework (Flask)
4. The yt-dlp package in Python was used, in conjunction with ffmpeg, to
    download only the audio and store it in the included 'Songs' folder
    (UPDATE: Now downloads directly to Apple Music)

Still to-do:

1. Clean up the front-end UI
    - Better-looking button
    - Fix the refresh bug
2. Make the server official (WSGI I think it was called); use different
    IP address, maybe localhost?
3. Clean up any remaining vulgar console.log() statements
4. Determine the method to get the downloaded music onto my phone
    - Could be a pre-existing app or possibly my own custom one

UPDATE 7/19/23: What has been accomplished

1. Overhauled the front-end UI; much better looking button
2. Updated server-side code to include the thumbnail as the music file icons
3. Hosting the music through Apple Music; works perfectly!
4. Re-downloaded summer playlist; icons now included, and used higher quality audio
5. Console.log()s all cleaned up

Still to-do:

1. Add a highlight and press effect to the button (UPDATE 7/20/23: Done!)
2. Fix refresh bug
3. Also, sometimes the thumbnail does not download; diagnose and solve
4. Make official server