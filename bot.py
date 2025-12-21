import requests
import os

TOKEN = os.environ.get("TOKEN_TELEGRAM")

print("TOKEN =", TOKEN)

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": 8271320198,
        "text": "TEST MESSAGE ✅ If you see this, Telegram works."
    }
)

