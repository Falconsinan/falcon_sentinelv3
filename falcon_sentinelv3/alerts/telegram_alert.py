import requests

def send_alert(token, chat_id, message):

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(url, data=data)