import os
from dotenv import load_dotenv
from pprint import pprint
import requests

os.system('mode con: lines=60')

load_dotenv()

URL = "https://api.weatherapi.com/v1/forecast.json"
PARAMS = {'q': '43206', 'days': 2, 'key': os.getenv('API_KEY')}

r = requests.get(url = URL, params = PARAMS)

data = r.json()
days = data['forecast']['forecastday']

#TODO make some indicator for current hour
for day in days:
    print(day['date'])
    hours = day['hour']
    for hour in hours:
        weather = [
            hour['time'],
            hour['temp_f'],
            hour['temp_c'],
            hour['condition']['text']
        ]
        pprint(weather)

input("Finished. Press Ctrl + C to end.")
