import os
import requests
import time

tokens_env = os.getenv("DISCORD_TOKENS", "")
channel_id = os.getenv("CHANNEL_ID")

tokens = [t.strip() for t in tokens_env.split(",") if t.strip()]
if not tokens:
    raise Exception("Thiếu token trong biến môi trường DISCORD_TOKENS")
if not channel_id:
    raise Exception("Thiếu biến môi trường CHANNEL_ID")

url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
data = {"content": "Test gửi tin nhắn đơn giản"}

for i, token in enumerate(tokens):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }
    res = requests.post(url, headers=headers, json=data)
    print(f"Token {i+1} status code:", res.status_code)
    print(f"Token {i+1} response:", res.text)
    time.sleep(1)  # Delay để tránh spam quá nhanh
