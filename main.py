import uuid

import requests

chatgpt_token = None


def get_livekit_url():
    headers = {
        "content-type": "application/json",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "authorization": "Bearer {}".format(chatgpt_token),
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

    # livekit url
    livekit_url = "https://meet.livekit.io"
    url = "{}/custom?liveKitUrl={}&token={}#{}".format(livekit_url, res["url"], res["token"], res["e2ee_key"])
    return url


if not chatgpt_token:
    print("Get ChatGPT Token: https://chatgpt.com/api/auth/session")
else:
    print(get_livekit_url())
