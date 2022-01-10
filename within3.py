#Python script for manipulating API result from a weather website
#Owner: Oluwaseun Winsala
#import modules
from flask import Flask, request 
import requests, json, os
 
#create an instance of flask app 
app = Flask(__name__)

#create a route to get the zip code of the city to check the weather
@app.route('/', methods=['GET'])

#Function to acess the API from the weather website
def weather():

#get the zip code from the browser
    zip_code = request.args.get('zip_code')
#base URL of the weather website
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
#API key retrieved from the weather website
    API_KEY = os.environ.get("API_KEY")
#complete URL to be used
    URL = base_url + "zip=" + zip_code + "&APPID=" + str(API_KEY)
#http request
    r = requests.get(f"{URL}")
#convert response to json format
    data = r.json()
#decouple the json data to retrieve needed variables  
    mainy = data['main']
    temperature = mainy['temp']
    temperature = str(round((temperature - 273.15) * 1.8 + 32)) + 'F'
    report = data['weather']
#convert needed response to json format   
    list_data = {
        "city": data['name'],
        "temp": temperature,
        "humidity": mainy['humidity'],
        "pressure": mainy['pressure'],
        "weather_report": report[0]['description']
    }

#return the resutling json to be displayed in a web browser
    return list_data
    
#other possibilities of display
    #return f"Current weather for {}", city 
    #return f"Current weather for {} is {}F with {} humidity of {} and pressure {}", city, temperature, climate, humidity, pressure
    #return f"The current weather for {city} is Temperature: {temperature}F, Humidity: {humidity}, Pressure: {pressure}, with {climate} "
    
        
#provide port and other parameters
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))   
    app.run(host="0.0.0.0", debug=True, port=port)
