import pandas as pd
import requests
from datetime import date
import os

TOKEN = os.environ.get("TOKEN_TELEGRAM")
MODE = os.environ.get("MODE")

DATE_DE_DEPART = date(2025, 8, 12)

def send(chat_id, text):
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": chat_id, "text": text}
    )

df = pd.read_csv("horaire.csv")

jour = 1

today = df[df["jour_cycle"] == jour]

for _, r in today.iterrows():
    nom = r["nom"]
    tache = r["tache"]
    chat = r["chat_id"]

    if MODE == "morning":
        if tache == "Free":
            msg = (
                f"Hello {nom} 👋\n\n"
                f"Today you are free 😄\n"
                f"Enjoy your day!"
            )
        else:
            msg = (
                f"Hello {nom} 👋\n\n"
                f"Your task for today is {tache}.\n"
                f"Good luck 💪"
            )
        send(chat, msg)

    if MODE == "cooking" and tache == "Cooking & Dishes":
        send(
            chat,
            f"Hello {nom} 👋\n\n"
            f"Reminder 🔔\n"
            f"Did you finish cooking and washing the dishes today? 🍽️"
        )

    if MODE == "cleaning" and tache == "Cleaning":
        send(
            chat,
            f"Hello {nom} 👋\n\n"
            f"Reminder 🔔\n"
            f"Did you finish cleaning today? 🧹"
        )
