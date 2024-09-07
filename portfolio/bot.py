import requests

def send_message(text):
    url = f"https://api.telegram.org/bot6531846833:AAEHJUbK9P2ydZsrgNuBC6MwwDAaf5ZLTdY/sendMessage"
    params = {"chat_id": '6214256605', "text": text}
    response = requests.post(url, data=params)
    return response.json()