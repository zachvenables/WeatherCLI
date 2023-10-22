import os
from dotenv import load_dotenv
from pprint import pprint
import requests
from datetime import datetime, timedelta

#TODO add some summary data
#TODO add a flexible header for days when AQI is not a thing

load_dotenv()

URL = "https://api.weatherapi.com/v1/forecast.json"
PARAMS = {'q': os.getenv('ZIP_CODE'), 'days': 3, 'key': os.getenv('API_KEY')}

response = requests.get(url = URL, params = PARAMS)

data = response.json()
days = data['forecast']['forecastday']

def print_header():
    print('\tTime\tTemp\t%Prec.\tCond.')
    print('\t------------------------------------------')

def get_hour(time):
    return time[-5:]

def hour_rounder(time):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    return (time.replace(second=0, microsecond=0, minute=0, hour=time.hour)
               +timedelta(hours=time.minute//30))

now = hour_rounder(datetime.now())

def is_current_hour(time):
    return time == str(now)[:-3]

get_next = True

for day in days:
    print(day['date'])
    print_header()
    hours = day['hour']
    for hour in hours:
        weather = ''
        weather += '\t' + get_hour(hour['time'])
        weather += '\t' + str(hour['temp_f'])
        
        weather += '\t' + str(hour['chance_of_rain']) + '%'
        weather += '\t' + hour['condition']['text']
        
        if is_current_hour(hour['time']):
            weather += ' <------- Current Hour'
        
        print(weather)
    print()
    inp = input("Press enter to see the following day's forecast. Type \'q\' to quit...\n")
    
    if(inp == 'q'):
        break
    