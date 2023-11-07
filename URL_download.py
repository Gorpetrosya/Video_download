import youtube_dl

# Replace this with the URL of the video you want to download
video_url = "https://www.dailymotion.com/video/x2gls63"

# Define options for youtube-dl (e.g., download format)
ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
