import requests
import json  

API_KEY = "ac3cd5575f5a2f600c8b09c335a11baf"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):

    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()  

        print("\nFull JSON response:")
        print(json.dumps(data, indent=4))  

        if data["cod"] != 200:
            print(f"\nError: {data['message']}")
        else:
            city = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"].capitalize()
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            print(f"\nWeather in {city}, {country}:")
            print(f"🌡️ Temperature: {temp}°C")
            print(f"☁️ Description: {description}")
            print(f"💧 Humidity: {humidity}%")
            print(f"💨 Wind Speed: {wind_speed} m/s\n")

    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
