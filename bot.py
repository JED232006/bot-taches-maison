import requests
import os

TOKEN = os.getenv("TOKEN_TELEGRAM")

CHAT_ID = 7508339230  # ton chat_id

message = "✅ TEST OK\n\nCe message confirme que le bot Telegram fonctionne 🚀"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": message
}

response = requests.post(url, data=data)

print("Status code:", response.status_code)
print("Response:", response.text)
