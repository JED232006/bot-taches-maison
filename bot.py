import pandas as pd
import requests
from datetime import date
import json

TOKEN = "${{ secrets.TOKEN_TELEGRAM }}"
DATE_DE_DEPART = date(2025, 12, 19)  # date de début du cycle

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
    if ligne["jour_cycle"] == jour_cycle:
        nom = ligne["nom"]
        tache = ligne["tache"]
        chat_id = ligne["chat_id"]

        # 🌞 MESSAGE DU MATIN
        if tache == "Cooking & Dishes":
            morning = (
                f"Hello {nom} 👋\n\n"
                f"Your task for today is Cooking & Dishes 🍳\n"
                f"Please remember to cook and wash all dishes after.\n\n"
                f"Good luck 💪"
            )
            envoyer_message(chat_id, morning)

        elif tache == "Cleaning":
            morning = (
                f"Hello {nom} 👋\n\n"
                f"Your task for today is Cleaning 🧹\n"
                f"Please make sure the house is clean and well organized.\n\n"
                f"Good luck 💪"
            )
            envoyer_message(chat_id, morning)

        else:
            morning = (
                f"Hello {nom} 👋\n\n"
                f"Today you are Free 😄\n"
                f"Enjoy your day and take some rest!"
            )
            envoyer_message(chat_id, morning)

        # 🌙 RAPPEL DU SOIR (pas pour Free)
        if tache in ["Cooking & Dishes", "Cleaning"]:

            question = (
                f"Hello {nom} 👋\n\n"
                f"Reminder 🔔\n"
                f"Did you finish your task today?"
            )

            buttons = [[
                {"text": "✅ YES", "callback_data": "yes"},
                {"text": "❌ NO", "callback_data": "no"}
            ]]

            envoyer_message(chat_id, question, buttons)

            follow_up = (
                "ℹ️ Please note:\n"
                "If you answered YES ✅, thank you for doing your task.\n"
                "If you answered NO ❌, please try to finish it as soon as possible 🙏"
            )

            envoyer_message(chat_id, follow_up)
