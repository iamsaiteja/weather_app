from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# HTML template
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Weather Now App</title>
</head>
<body>
    <h5>   ===> Weather Now App 🌤️ <===   </h5>
    <form method="post">
        Enter City: <input type="text" name="city">
        <button type="submit">Get Weather</button>
    </form>

    {% if weather %}
        <h3>Weather in {{ city }}</h3>
        <p>Temperature: {{ weather['temperature'] }} °C</p>
        <p>Windspeed: {{ weather['windspeed'] }} km/h</p>
        <p>Weather Code: {{ weather['weathercode'] }}</p>
        <p>Time: {{ weather['time'] }}</p>
    {% endif %}
</body>
</html>
"""

def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {"latitude": lat, "longitude": lon, "current_weather": True}
    response = requests.get(url, params=params)
    return response.json().get("current_weather", None)

# Example city coordinates
city_coords = {
    "Hyderabad": (17.385044, 78.486671),
    "Delhi": (28.7041, 77.1025),
    "Mumbai": (19.0760, 72.8777)
}

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    city = None
    if request.method == "POST":
        city = request.form["city"]
        if city in city_coords:
            lat, lon = city_coords[city]
            weather = get_weather(lat, lon)
    return render_template_string(html, weather=weather, city=city)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


