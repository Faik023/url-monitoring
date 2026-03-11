# URL Monitoring Bot

Python script that monitors websites and sends Telegram alerts if a site goes down.

## Features

* Website uptime monitoring
* Telegram notifications when a site fails
* Configurable check interval
* Multiple URLs support
* Logging system

## How it works

The script periodically checks a list of URLs.
If any website becomes unavailable or returns an error status, the bot sends an alert message to Telegram.

## Configuration

Create `config.json` based on `config.example.json`.

Example:

```json
{
  "urls": [
    "https://google.com",
    "https://github.com"
  ],
  "check_interval": 60,
  "telegram_bot_token": "YOUR_BOT_TOKEN",
  "telegram_chat_id": "YOUR_CHAT_ID"
}
```

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/url-monitoring.git
cd url-monitoring
```

Install dependencies:

```
pip install -r requirements.txt
```

## Run

```
python monitor.py
```

## Use case

This bot is useful for:

* website uptime monitoring
* server monitoring
* project health checks
* simple DevOps automation

## Tech Stack

* Python
* Requests
* Telegram Bot API
