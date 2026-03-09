import json
import time
import requests
import logging
def send_telegram_alert(bot_token, chat_id, message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        requests.post(url, json=payload)
    except Exception as e:
        logging.error(f"Telegram alert failed: {e}")

# Настройка логирования
logging.basicConfig(
    filename="monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def load_config():
    with open("config.json", "r") as file:
        return json.load(file)


def check_urls(urls):
    errors = []

    for url in urls:
        try:
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                logging.info(f"{url} OK")
                print(f"{url} OK")
            else:
                logging.error(f"{url} ERROR {response.status_code}")
                errors.append(f"{url} returned {response.status_code}")

        except requests.RequestException as e:
            logging.error(f"{url} FAILED {e}")
            errors.append(f"{url} FAILED")

    return errors


def main():
    config = load_config()

    urls = config["urls"]
    interval = config["check_interval"]
    bot_token = config["telegram_bot_token"]
    chat_id = config["telegram_chat_id"]

    while True:
        print("Checking URLs...")

        errors = check_urls(urls)

        if errors:
            message = "⚠ Website monitoring alert!\n\n"

            for error in errors:
                message += f"{error}\n"

            print(message)

            send_telegram_alert(bot_token, chat_id, message)
        else:
            print("All sites are OK")

        time.sleep(interval)


if __name__ == "__main__":
    main()