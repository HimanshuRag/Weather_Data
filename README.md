# Weather_Fetcher
This Python script allows users to quickly fetch and display current weather information for any city in the world using the OpenWeatherMap API. By simply providing a city name, the script retrieves real-time data such as temperature, humidity, weather description, and wind speed.

How It Works
OpenWeatherMap API
The script utilizes the OpenWeatherMap API to query and fetch weather data in JSON format. To use this API, you will need a valid API key, which can be obtained by creating a free account on OpenWeatherMap.

Main Flow

main() prompts the user to input the name of the city they want weather information for.
get_weather(city_name) constructs the request URL, makes the API call, and returns the weather data as JSON if successful.
display_weather(data) takes the JSON response and prints the relevant weather details in a readable format.
Program Structure

get_weather(city_name)
Builds a complete URL with query parameters (city name, API key, and units in metric).
Makes an HTTP GET request to the OpenWeatherMap API.
Returns the JSON data if the response is successful (status code 200); otherwise, prints an error message and returns None.
display_weather(data)
Extracts the city name, temperature, humidity, weather description, and wind speed from the JSON response.
Prints the weather information in a user-friendly format.
main()
Asks the user to input a city name.
Calls get_weather() with the user-provided city name to fetch the weather data.
Passes the weather data to display_weather() for presentation.
Prerequisites
Python 3.6+
Ensure you have Python 3.6 or higher installed on your system.
Requests Library
This script uses the requests library to make HTTP requests. If you do not have it installed, run:
bash
Copy code
pip install requests
OpenWeatherMap API Key
Sign up at OpenWeatherMap.
Go to your profile and navigate to the “API keys” section.
Copy your unique API key and replace the placeholder in the code.
Usage
Clone or Download
Clone this repository or download the script to your local machine:

bash
Copy code
git clone https://github.com/yourusername/weather-fetcher.git
Navigate and Run
Open a terminal (or command prompt) in the script’s directory and run:

bash
Copy code
python weather_fetcher.py
Enter City Name
When prompted, type the name of the city you want to fetch the weather for (e.g., "New York") and press Enter.

View Results
The script will display the weather information in the following format:

yaml
Copy code
Request URL: http://api.openweathermap.org/data/2.5/weather?q=New York&appid=YOUR_API_KEY&units=metric

Weather in New York:
Temperature: 25.4°C
Humidity: 65%
Weather Description: Clear sky
Wind Speed: 3.5 m/s
Customization
Units
You can change the units=metric parameter in the get_weather() function to other options like imperial for Fahrenheit.
Languages
If you want localized weather descriptions, you can add a language parameter (e.g., &lang=es for Spanish) to the query URL.
Contributing
Feel free to fork this project and submit a pull request if you have any improvements or suggestions.

License
This project is licensed under the MIT License.
