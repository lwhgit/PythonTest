import json
import requests

DEVELOPER_KEY = "AIzaSyCiBzYtWNgRXZWs5w2zqtp4Lqfve5GyGCY"

def yt_video(videoId):
    results = requests.get("https://www.googleapis.com/youtube/v3/videos", 
        params = {
            "id": videoId,
            "part": "id,snippet,contentDetails",
            "key": DEVELOPER_KEY
        })


    data = results.json()["items"][0]
    
    video = {
        "title": data["snippet"]["title"],
        "thumbnails": data["snippet"]["thumbnails"],
        "videoId": data["id"],
        "duration": data["contentDetails"]["duration"]
    }
    
    return video

print(yt_video("mAKsZ26SabQ"))