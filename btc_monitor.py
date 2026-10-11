import os
import time
import requests
import ccxt
from dotenv import load_dotenv

# Load secret environment variables from .env file
load_dotenv()

# ==================== SECURE CONFIGURATION ==================== #
SYMBOL = "BTC/USDT"
LOWER_BOUND = 83000.0  # Bottom of target demand zone
UPPER_BOUND = 83200.0  # Top of target demand zone
POLL_INTERVAL = 10     # Poll every 10 seconds

# Fetch private keys securely from environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
# ============================================================== #

# Initialize CCXT Binance instance (public data endpoint)
exchange = ccxt.binance({
    'enableRateLimit': True,
})

def send_telegram_alert(message: str):
    """Sends a push notification using secure environment credentials."""
    if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
        try:
            requests.post(url, json=payload, timeout=5)
        except Exception as e:
            print(f"[!] Failed to send Telegram alert: {e}")
    else:
        print("[!] Telegram credentials missing in .env file. Running in console-only mode.")

def monitor_demand_zone():
    print(f"[*] Starting BTC/USDT Price Monitor using CCXT v{ccxt.__version__}")
    print(f"[*] Target Demand Zone: ${LOWER_BOUND:,.2f} -${UPPER_BOUND:,.2f}")
    print("[*] Monitoring public market feed...\n")

    while True:
        try:
            ticker = exchange.fetch_ticker(SYMBOL)
            current_price = ticker['last']
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

            print(f"[{timestamp}] BTC Spot Price: ${current_price:,.2f}")

            if LOWER_BOUND <= current_price <= UPPER_BOUND:
                alert_msg = (
                    f"🚨 *BTC Demand Zone Entry ALERT!*\n\n"
                    f"• *Current Spot:* `${current_price:,.2f}`\n"
                    f"• *Target Zone:* `${LOWER_BOUND:,.2f} - ${UPPER_BOUND:,.2f}`\n"
                    f"• *Execution:* Evaluate Bullish Swing Setup."
                )
                
                print("\n" + "="*55)
                print(f"[ALERT TRIGGERED] BTC Entered Zone - Current Price: ${current_price:,.2f}")
                print("="*55 + "\n")

                send_telegram_alert(alert_msg)

                # Cooldown period to avoid spamming alerts
                time.sleep(300)

            time.sleep(POLL_INTERVAL)

        except ccxt.NetworkError as e:
            print(f"[!] Network Error: {e}. Retrying in 15 seconds...")
            time.sleep(15)
        except ccxt.ExchangeError as e:
            print(f"[!] Exchange Error: {e}. Retrying in 15 seconds...")
            time.sleep(15)
        except KeyboardInterrupt:
            print("\n[*] Monitor stopped by user.")
            break
        except Exception as e:
            print(f"[!] Unexpected error: {e}")
            time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    monitor_demand_zone()