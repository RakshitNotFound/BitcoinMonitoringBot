# 🚀 Bitcoin Demand Zone Monitor Bot

A lightweight, autonomous Python monitoring bot that tracks live BTC/USDT spot prices using the `ccxt` library and sends real-time Telegram alerts when the price enters a specified "buy-the-dip" demand zone.

---

## 📌 Features

* **Real-time Price Tracking:** Polls live market data from Binance via ccxt.
* **Automated Telegram Alerts:** Delivers instant push notifications directly to your phone when prices drop into your target price window.
* **Alert Cooldown:** Built-in sleep timer to prevent spamming notifications while price bounces inside the target zone.
* **Secure Credentials:** Keeps Telegram bot tokens and chat IDs isolated in a .env file to prevent accidental leaks on public repositories.

---

## 🛠️ Project Structure

BitcoinMonitor/
├── btc_monitor.py    # Main monitoring script
├── .env              # Environment variables (Ignored by Git)
├── .gitignore        # Excludes sensitive files from version control
└── README.md         # Documentation

---

## 🚀 Getting Started

### 1. Prerequisites

Make sure you have Python installed on your machine along with the required libraries:

`pip install ccxt python-dotenv requests`

### 2. Set Up Telegram Credentials

1. Open Telegram and search for `@BotFather` to create a new bot and copy your **Bot Token**.
2. Search for `@userinfobot` on Telegram to get your personal **Chat ID**.
3. Create a `.env` file in the root directory of this project and add your credentials:

TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here  
TELEGRAM_CHAT_ID=your_telegram_chat_id_here  

---

## ⚙️ Usage

Run the script locally using terminal or VS Code:

`python btc_monitor.py`

---

## 🔒 Security

This repository utilizes `.gitignore` to ensure `.env` is never pushed to public version control. **Never commit your live API keys or bot tokens directly into your source code.**
