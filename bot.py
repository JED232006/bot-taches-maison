import requests
import os

TOKEN = "8536945340:AAHzXOhWcjEWnvzPlT2o3xv2MRsKUM4a9V8"

print("TOKEN =", TOKEN)

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id":8271320198,
        "chat_id":8271320198,
        "text": "TEST MESSAGE ✅ If you see this, Telegram works."
    }
)

