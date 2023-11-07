import requests
import youtube_dl


video_id_list = []
for i in range(1,9):
    x = requests.get(f"https://api.dailymotion.com/user/jahaz1500/videos?limit=100&page={i}")
    for j in x.json()["list"]:
        video_id_list.append("https://www.dailymotion.com/video/" + j["id"])



for i in video_id_list:
    video_url = i

    ydl_opts = {}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])