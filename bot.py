import requests
import os
from datetime import datetime

# =========================
# CONFIG
# =========================
TOKEN = os.getenv("TOKEN_TELEGRAM")

CHAT_IDS = {
    "jed": 7508339230,
    "yves": 7431839058,
    "derek": 8271320198
}

# =========================
# TIME (GitHub = UTC)
# =========================
now = datetime.utcnow()
hour = now.hour  # UTC

# =========================
# MESSAGE LOGIC
# =========================
if hour == 4:
    message = "☀️ BONJOUR !\n\nVoici les tâches du matin 🧹"
elif hour == 18:
    message = "🍽️ RAPPEL 21H\n\nCooking & Dishes + Cleaning 🧼"
else:
    print("⏱️ Aucun message à envoyer maintenant")
    exit()

# =========================
# SEND MESSAGE
# =========================
for name, chat_id in CHAT_IDS.items():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }

    r = requests.post(url, data=data)

    if r.status_code == 200:
        print(f"✅ Message envoyé à {name}")
    else:
        print(f"❌ Erreur pour {name}: {r.text}")
