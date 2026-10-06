import time
import requests
import RPi.GPIO as GPIO
import os
from dotenv import load_dotenv # import the load_dotenv function

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Telegram information
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("Alert button monitoring system is now active. Press Ctrl+C to stop.")

button_pressed = False
try:
	while True:
		if GPIO.input(7) == GPIO.HIGH and not button_pressed:
			print("Someone pressed the alert button!")
			url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
			data = {
				"chat_id": CHAT_ID,
				"text": "Someone pressed the alert button!"
			}

			response = requests.post(url, data=data)
			print("Telegram status:", response.status_code)
			print("Telegram response:", response.text)

			button_pressed = True

		elif GPIO.input(7) == GPIO.LOW:
			button_pressed = False
		time.sleep(0.1)
except KeyboardInterrupt:
	print("\nMonitoring stopped.")
	GPIO.cleanup()
