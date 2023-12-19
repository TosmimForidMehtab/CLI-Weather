import argparse
import pyfiglet
from simple_chalk import chalk
import requests
from constants import *

parser = argparse.ArgumentParser(description="Get weather information for a city/country")
parser.add_argument("country", help="Country/City to get weather information")
args = parser.parse_args()

url = f"{BASE_URL}?q={args.country}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code != 200:
    print(chalk.red("Error: Could not get weather information."))
    exit(1)

data = response.json()
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

weather_icon = WEATHER_ICONS.get(icon, "❓")
output = f"{pyfiglet.figlet_format(city)}{country}\n\n"
output += f"{weather_icon}  {description}\n"
output += f"Temperature: {temperature}°C\n"
output += f"Feels like: {feels_like}°C\n"

print(chalk.cyan(output))