import requests

def get_weather(city, latitude, longitude):
    # Open-Meteo API endpoint
    url = "https://api.open-meteo.com/v1/forecast"

    # Parameters for the API call
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise error for bad response

        data = response.json()
        if "current_weather" in data:
            weather = data["current_weather"]
            print(f"Weather in {city}:")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Windspeed: {weather['windspeed']} km/h")
            print(f"Weather Code: {weather['weathercode']}")
            print(f"Time: {weather['time']}")
        else:
            print("No current weather data available.")
    except Exception as e:
        print("Error fetching weather:", e)


# Example city with coordinates (Hyderabad)
city = "Hyderabad"
latitude = 17.385044
longitude = 78.486671

get_weather(city, latitude, longitude)
