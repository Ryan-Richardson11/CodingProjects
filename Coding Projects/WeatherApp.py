import requests
import json

# API endpoint and parameters
url = 'https://api.openweathermap.org/data/2.5/weather'
api_key = '0bbaa3f885626f607b022005b2381258'
units = 'metric'

# Prompt user to input location
location = input("Enter a city name: ")

# Send HTTP request to API endpoint
params = {'q': location, 'appid': api_key, 'units': units}
response = requests.get(url, params=params)

# Parse API response
weather_data = json.loads(response.text)

# Extract relevant weather data
temperature = weather_data['main']['temp']
description = weather_data['weather'][0]['description']

# Display weather data to user
print(f"Current temperature in {location} is {temperature:.2f} degrees Celsius")
print(f"Description: {description}")