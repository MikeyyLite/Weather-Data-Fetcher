# Weather Data Integration using OpenWearherMap API
## About the project
This Python script interacts with the OpenWeatherMap API to fetch and display weather information based on latitude and longitude. This script gives out all relevant weather data that could be further integrated into various applications.

## Functionality
1. **Fetch Weather Data:**
    - Accepts latitude and longitude as input from the user.
    - Uses the [OpenWeatherMap API](https://openweathermap.org/current) to fetch the current weather data for the specified latitude and longitude.

2. **The following details about the weather are displayed:**
    * Latitude and Longitude
    * Temperature 
    * Weather Description (e.g., "clear sky", "light rain")
    * Humidity Percentage
    * Wind Speed 
3. **Error Handling:**
    * Handles cases where the API request fails or longitude and latitude are incorrect.
    * Prints appropriate error messages to inform the user.

## Built with
The following tools were used to build this python script
*  [requests](https://pypi.org/project/requests/) : This python library was used to make API calls to OpenWeatherMap API
* [OpeWeatherMap API](https://openweathermap.org/current): This free API by OpenWeather was used to fetch current weather conditions of a location. It allows making one call at a time for a particular latitude and longitude
* [Python 3.12.4](https://www.python.org/downloads/release/python-3124/): Python version 3.12.4 was used to build this script

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/MikeyyLite/weather-data-fetcher.git
   cd weather-data-fetcher

2. **Set up your own API Key**
- Register at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to get your API key.
- Replace the placeholder **your_api_key** in the script with your actual API key.
3. **Install Dependencies**<br>
Make sure you have Python installed. Install the required package by running:
    ```bash
    pip install requests

## Usage

1. **Run the Program**

   To start the program, run the following command:

   ```bash
   python weather_data_fetcher.py

2. **Input Latitude and Longitude**

   - You will be prompted to enter a valid latitude and longitude.
   - The latitude should be between -90 and +90.
   - The longitude should be between -180 and +180.
   - If you enter invalid or empty values, the program will notify you and prompt you to enter the coordinates again.

3. **View Weather Data**

   Once you provide valid coordinates, the program will display the following weather information:
   - **Location Name:** The name of the nearest city or location.
   - **Latitude:** The latitude you provided.
   - **Longitude:** The longitude you provided.
   - **Temperature:** The current temperature in Celsius.
   - **Weather:** A brief description of the current weather (e.g., clear sky, rain).
   - **Humidity:** The current humidity level as a percentage.
   - **Wind Speed:** The current wind speed in meters per second (m/s).

3. **Example**

   Here's an example of what the output might look like:
   ```bash
   This program gives weather data based on Latitude and Longitude inputs.  
    Valid ranges for inputs are:  
        Latitude: -90 to +90  
        Longitude: -180 to +180  

    Enter Latitude:40.7128  
    Enter Longitude:-74.0060

    New York Weather Data
    Latitude: 40.7128  
    Longitude: -74.0060  
    Temperature: 20.5 °C  
    Weather:clear sky  
    Humidity:60%  
    Wind Speed:3.1 m/s  

    -----------------------------------
    Do you wish to continue? Y/N :

