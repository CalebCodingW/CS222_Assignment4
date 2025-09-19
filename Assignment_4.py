import json
import ssl
from urllib.request import urlopen

def main():
    latitude = 40.1934
    longitude = -85.3864
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    context = ssl._create_unverified_context()
    response = urlopen(url, context = context)
    data = json.loads(response.read())
    weatherUrl = data["properties"]["forecast"]
    response = urlopen(weatherUrl, context = context)
    weatherData = json.loads(response.read())
    print(len(weatherData["properties"]["periods"]))
    for event in weatherData["properties"]["periods"]:
        print(event["name"])
        print(event["temperature"])
        print(event["detailedForecast"])
main()