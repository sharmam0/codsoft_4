def get_weather_data(city):
    # API endpoint and parameters
    url = f'http://api.weatherapi.com/v1/current.json'
    params = {
        'key': 'your_api_key',
        'q': city,
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Extract relevant weather information
    if 'error' in data:
        return None
    location = data['location']['name']
    temperature = data['current']['temp_c'] # Use 'temp_f' for Fahrenheit
    humidity = data['current']['humidity']
    wind_speed = data['current']['wind_kph']
    condition = data['current']['condition']['text']

    # Return weather data
    return {
        'location': location,
        'temperature': temperature,
        'humidity': humidity,
        'wind_speed': wind_speed,
        'condition': condition
    }


def display_weather(weather_data):
    if weather_data is None:
        print("Failed to fetch weather data.")
    else:
        print("Location:", weather_data['location'])
        print("Temperature:", weather_data['temperature'], "°C")
        print("Humidity:", weather_data['humidity'], "%")
        print("Wind Speed:", weather_data['wind_speed'], "km/h")
        print("Condition:", weather_data['condition'])


def main():
    city = input("Enter city name: ")
    weather_data = get_weather_data(city)
    display_weather(weather_data)

    main()