import requests

# Function to check if the provided latitude and longitude are valid
def is_valid_lat_lon(lat, lon):
    try:
        lat = float(lat)  # Convert latitude to a float
        lon = float(lon)  # Convert longitude to a float
    except ValueError:
        return False  # If conversion fails, the input is not valid

    # Check if the latitude is between -90 and +90 and longitude is between -180 and +180
    return (-90 <= lat <= 90) and (-180 <= lon <= 180)

# Introduction message with valid ranges for latitude and longitude
print('\nThis program gives weather data based on Latitude and Longitude inputs. \nValid ranges for inputs are: \n  #Latitude  : -90 to +90 \n  #Longitude : -180 to +180')

# Loop to allow the user to enter multiple sets of coordinates
loop = True
while(loop):
    # User input for latitude and longitude
    lat = input("Enter Latitude:")
    lon = input("Enter Longitude:")

    # Check for empty inputs
    if not (lat) or not (lon):
        print('-------------------------------------------------------------------') 
        print('Error: No coordinates provided. Please enter latitude and longitude') 
        print('-------------------------------------------------------------------') 

    # Check if the latitude and longitude are within valid ranges
    elif not is_valid_lat_lon(lat, lon):
        print('-------------------------------------------------------------------') 
        print('Error: Unable to retrieve weather data. Please check the coordinates and try again.')  
        print('-------------------------------------------------------------------') 
  
    else:
       
        your_api_key = '5d5b0874f3adb7ae5098d4e7ab3c1b8a'
        
        # Making a request to the OpenWeatherMap API with the provided latitude and longitude
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={your_api_key}&units=metric')

        # Check if the request is invalid (e.g., bad request)
        if(response.status_code == 400):
            print("Error : Invalid Request")
            continue
        # Check if the server failed to process a valid request
        elif(response.status_code == 500):
            print("Error : Server failed to fulfill a valid request due to an error with server")    
            continue

        # Extracting weather data from the API response
        latitude = response.json()['coord']['lat']
        longitude = response.json()['coord']['lon']
        temperature = response.json()['main']['temp']
        weather = response.json()['weather'][0]['description']
        humidity = response.json()['main']['humidity']
        wind = response.json()['wind']['speed']

        # Printing the weather data
        print(f"\n{response.json()['name']} Weather Data")
        print(f'Latitude: {latitude}')
        print(f'Longitude: {longitude}')
        print(f'Temperature: {temperature} °C')
        print(f'Weather: {weather}')
        print(f'Humidity: {humidity}%')
        print(f'Wind Speed: {wind}m/s')
        print('-------------------------------------------------------------------')

      
        a = input('Do you wish to continue? Y/N : ')


        if (a == 'n' or a == 'N'):
            loop = False
        
        print('-------------------------------------------------------------------')
