import os
from dotenv import load_dotenv
from pprint import pprint
import requests
from datetime import datetime, timedelta

#TODO add chance of rain
#TODO add some summary data
#TODO add AQI info
#TODO add keypress for next day's weather



load_dotenv()

URL = "https://api.weatherapi.com/v1/forecast.json"
PARAMS = {'q': '43206', 'days': 3, 'key': os.getenv('API_KEY')}

response = requests.get(url = URL, params = PARAMS)

data = response.json()
days = data['forecast']['forecastday']

def print_header():
    print('\n\tTime\tTemp\tCond.')
    print('\t---------------------\n')

def get_hour(time):
    return time[-5:]

def hour_rounder(time):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    return (time.replace(second=0, microsecond=0, minute=0, hour=time.hour)
               +timedelta(hours=time.minute//30))

now = hour_rounder(datetime.now())

def is_current_hour(time):
    return time == str(now)[:-3]

for day in days:
    print(day['date'])
    print_header()
    hours = day['hour']
    for hour in hours:
        weather = ''
        
        weather += '\t' + get_hour(hour['time']) + '\t' + str(hour['temp_f']) + '\t' + hour['condition']['text']
        
        if is_current_hour(hour['time']):
            weather += ' <------- Current Hour'
        
        print(weather)
    print()
        
input("Finished. Press Enter to end.")
