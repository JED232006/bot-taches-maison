import pandas as pd
import requests
import os
from datetime import date

TOKEN = os.getenv("TOKEN_TELEGRAM")
MODE = os.getenv("MODE")

CSV_FILE = "horaire.csv"

# Jour automatique (1 → 21 → recommence)
today = date.today()
day_number = (today.toordinal() % 21) or 21

df = pd.read_csv(CSV_FILE)
today_tasks = df[df["day"] == day_number]

def send(chat_id, message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": chat_id, "text": message})

for _, row in today_tasks.iterrows():
    name = row["person"]
    task = row["task"]
    chat_id = row["chat_id"]

    # 🌅 MESSAGE DU MATIN (07:00)
    if MODE == "morning":
        if task == "Free":
            msg = (
                f"Good morning {name} 👋\n\n"
                "Today you are free 😄\n"
                "Enjoy your day!"
            )
        else:
            msg = (
                f"Good morning {name} 👋\n\n"
                f"Your task for today is: {task}\n"
                "💪 Good luck!"
            )
        send(chat_id, msg)

    # 🌙 RAPPELS DU SOIR (21:00)
    elif MODE == "evening":
        if task == "Cooking & Dishes":
            msg = (
                f"🍽️ Evening reminder {name}!\n\n"
                "Don't forget your task:\n"
                "Cooking & Dishes 👨‍🍳"
            )
            send(chat_id, msg)

        elif task == "Cleaning":
            msg = (
                f"🧹 Evening reminder {name}!\n\n"
                "Don't forget your task:\n"
                "Cleaning 🧼"
            )
            send(chat_id, msg)
