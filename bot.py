import pandas as pd
import requests
from datetime import date
import json
import os

TOKEN = os.environ.get("TOKEN_TELEGRAM")
MODE = os.environ.get("MODE")  # morning | cleaning | cooking
DATE_DE_DEPART = date(2025, 12, 21)

def envoyer_message(chat_id, message, buttons=None):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": message}

    if buttons:
        data["reply_markup"] = json.dumps({"inline_keyboard": buttons})

    requests.post(url, data=data)

df = pd.read_csv("horaire.csv")

jours_passes = (date.today() - DATE_DE_DEPART).days
jour_cycle = (jours_passes % 21) + 1

for _, ligne in df.iterrows():
    if ligne["jour_cycle"] != jour_cycle:
        continue

    nom = ligne["nom"]
    tache = ligne["tache"]
    chat_id = ligne["chat_id"]

    # 🌞 MATIN
    if MODE == "morning":
        if tache == "Cooking & Dishes":
            envoyer_message(chat_id,
                f"Hello {nom} 👋\n\n"
                f"Your task for today is Cooking & Dishes 🍳\n"
                f"Please remember to cook and wash all dishes after.\n\n"
                f"Good luck 💪"
            )

        elif tache == "Cleaning":
            envoyer_message(chat_id,
                f"Hello {nom} 👋\n\n"
                f"Your task for today is Cleaning 🧹\n"
                f"Please make sure the house is clean and well organized.\n\n"
                f"Good luck 💪"
            )

        else:
            envoyer_message(chat_id,
                f"Hello {nom} 👋\n\n"
                f"Today you are Free 😄\n"
                f"Enjoy your day and take some rest!"
            )

    # 🧹 RAPPEL CLEANING – 19h
    if MODE == "cleaning" and tache == "Cleaning":
        envoyer_message(chat_id,
            f"Hello {nom} 👋\n\n"
            f"Reminder 🔔\n"
            f"Did you finish cleaning the house today? 🧹",
            [[{"text": "✅ YES", "callback_data": "yes"},
              {"text": "❌ NO", "callback_data": "no"}]]
        )

    # 🍳 RAPPEL COOKING – 21h
    if MODE == "cooking" and tache == "Cooking & Dishes":
        envoyer_message(chat_id,
            f"Hello {nom} 👋\n\n"
            f"Reminder 🔔\n"
            f"Did you finish cooking and washing the dishes today? 🍽️",
            [[{"text": "✅ YES", "callback_data": "yes"},
              {"text": "❌ NO", "callback_data": "no"}]]
        )
