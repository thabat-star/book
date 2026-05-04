import os
import requests

email = os.getenv("EMAIL")
file_name = os.getenv("FILE_NAME")
file_path = os.getenv("FILE_PATH")

token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("CHAT_ID")

text = f"""
📩 New Form Submission

Email: {email}
File Name: {file_name}
File Path: {file_path}
"""

url = f"https://api.telegram.org/bot{token}/sendMessage"

requests.post(url, data={
    "chat_id": chat_id,
    "text": text
})
