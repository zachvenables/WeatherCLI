import os
from dotenv import load_dotenv
from pprint import pprint
import requests

load_dotenv()

URL = "https://api.weatherapi.com/v1/forecast.json"
PARAMS = {'q': '43206', 'days': 3, 'key': os.getenv('API_KEY')}

r = requests.get(url = URL, params = PARAMS)

data = r.json()
days = data['forecast']['forecastday']
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
