import sys
from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('NUTRITION_API_KEY')
APP_ID = os.environ.get('NUTRITION_APP_ID')

endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

user_activity = input("Enter details about your activity:\n ")

request_config = {
    "query": user_activity
}

response = requests.post(url=endpoint, json=request_config, headers=headers)
current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")
response_json = response.json()


sheety_endpoint = 'https://api.sheety.co/aae6f5b087b40c08e5a4a2addfb2587a/100DaysofpythonDay38/workouts'
SHEETY_AUTH_TOKEN = os.environ.get('SHEETY_AUTH_TOKEN')

for ex in response_json["exercises"]:
    sheety_request_body = {
            "workout": {
                "date": current_date,
                "time": current_time,
                "exercise": ex["name"].title(),
                "duration": ex["duration_min"],
                "calories": ex["nf_calories"]
            }
    }

    sheety_headers = {"Authorization": SHEETY_AUTH_TOKEN}
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_request_body, headers=sheety_headers)



