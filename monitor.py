import os
import time
import json
import requests
from dotenv import load_dotenv

# загружаем .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    print("ERROR: BOT_TOKEN not found in .env")
    exit()

CONFIG_FILE = "config.json"
LOG_FILE = "monitor.log"


def log(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"

    print(line)

    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def send_message(chat_id, text):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        data = {
            "chat_id": chat_id,
            "text": text
        }

        requests.post(url, data=data, timeout=10)

    except Exception as e:
        log(f"Telegram error: {e}")


def load_config():
    try:
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    except Exception as e:
        log(f"Config error: {e}")
        exit()


def check_url(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except:
        return False


def main():

    config = load_config()

    urls = config["urls"]
    interval = config["check_interval"]
    chat_id = config["chat_id"]

    log("URL Monitor started")

    while True:

        for url in urls:

            status = check_url(url)

            if status:
                log(f"{url} OK")
            else:
                log(f"{url} DOWN")

                message = f"⚠️ Website DOWN: {url}"
                send_message(chat_id, message)

        time.sleep(interval)


if __name__ == "__main__":
    main()