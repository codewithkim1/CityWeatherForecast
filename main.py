import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        return f"The current weather in {city} is {temperature}°C with {description}."
    elif response.status_code == 401:
        return "Invalid API key. Please check your OpenWeatherMap API key."
    elif response.status_code == 404:
        return f"City '{city}' not found. Please check the city name and try again."
    else:
        return f"Failed to fetch weather data for {city}. Please try again later."

def main():
    print("Welcome to the City Weather Checker!")

    # Input your OpenWeatherMap API key here
    api_key = "enter_your_api_key"

    while True:
        city = input("Enter the city name (or 'exit' to quit): ")

        if city.lower() == 'exit':
            print("Exiting the City Weather Checker. Goodbye!")
            break

        result = get_weather(api_key, city)

        print("\nResult:")
        print(result)
        print()

if __name__ == "__main__":
    main()
