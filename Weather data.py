import requests

# Your actual API key from OpenWeatherMap
API_KEY = '6e82d04347103e7f3db1ea59cae49f27'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city_name):
    """
    Fetch weather data from OpenWeatherMap for the given city.
    """
    complete_url = f"{BASE_URL}q={city_name}&appid={API_KEY}&units=metric"
    
    # Print the request URL for debugging (optional)
    print(f"Request URL: {complete_url}")
    
    # Make the GET request to the OpenWeatherMap API
    response = requests.get(complete_url)
    
    # If the request is successful, return the JSON data
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data. Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

def display_weather(data):
    """
    Display weather information fetched by the API.
    """
    if data:
        city_name = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        
        print(f"\nWeather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {weather_description.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s\n")
    else:
        print("Could not retrieve weather data.")

def main():
    """
    Main function to get user input (city name) and display weather details.
    """
    # Get the city name from the user
    city_name = input("Enter the city name: ")
    
    # Fetch the weather data
    weather_data = get_weather(city_name)
    
    # Display the weather data
    display_weather(weather_data)

if __name__ == "__main__":
    main()
