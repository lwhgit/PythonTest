import os
import requests

DEVELOPER_KEY = "AIzaSyCiBzYtWNgRXZWs5w2zqtp4Lqfve5GyGCY"

PATH = os.path.dirname(os.path.realpath(__file__))

def gt_tts(q, lang, path):
    results = requests.get("https://translate.google.com/translate_tts", 
        params = {
            "q": q,
            "ie": "UTF-8",
            "tl": lang,
            "client": "tw-ob"
        })
        
    f = open(path, "wb")
    f.write(results.content)
    f.close()

gt_tts("test", "ko", PATH + "\\tts.mp3")