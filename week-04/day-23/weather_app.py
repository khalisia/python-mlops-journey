import requests

# Nairobi is the city of choice

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=-1.2864"
    "&longitude=36.8172"
    "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)
response = requests.get(url)
# Reading the json
if response.status_code == 200:

    data = response.json()

    #Extracting the relevant values

    current = data["current"]

    temperature = current["temperature_2m"]
    humidity = current["relative_humidity_2m"]
    wind = current["wind_speed_10m"]

    #Displaying the results

    print("Current Weather\n")

    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind} km/h")

else:
    print("Failed to retrieve weather data")
