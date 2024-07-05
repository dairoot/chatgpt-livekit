import uuid

import requests

token = "替换为自己的 ChatGPT Token：获取地址：https://chatgpt.com/api/auth/session"

headers = {
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "authorization": "Bearer {}".format(token),
}

res = requests.post("https://chatgpt.com/voice/get_token", headers=headers, cookies={'__cf_bm': ''}, json={
    "voice": "cove",
    "voice_mode": "standard",
    "parent_message_id": str(uuid.uuid4()),
    "model_slug": "auto",
    "voice_training_allowed": False,
    "enable_message_streaming": False,
    "language": "zh",
    "video_training_allowed": False,
    "voice_session_id": str(uuid.uuid4())
}).json()

# livekit 官方地址 
livekit_url = "https://meet.livekit.io/custom?liveKitUrl={}&token={}#{}".format(
    res["url"], res["token"], res["e2ee_key"])
print(livekit_url)
