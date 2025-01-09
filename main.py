import requests
from tg_send_text import send_tg_message
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

API = "https://api.openweathermap.org/data/2.5/forecast?"

parameters = {
    "lat": 47.497913,
    "lon": 19.040236,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url=API, params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    send_tg_message("Bring an umbrella!")
    print("bring an umbrella!")
