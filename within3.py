#Python script for manipulating API result from a weather website

#importing modules
from flask import Flask, request 
import requests, json, os
 
#create an instance of flask app 
app = Flask(__name__)

#using the zip code from the vars in Heroku
#zip_code = str(os.environ["ZIP_CODE"])
#@app.route('/<string:{zip_code}>', methods=['GET'])

#zip_code = 32901
#creating a route to get the zip code of the city to check the weather
#@app.route('/<string:zip_code>', methods=['GET'])
@app.route('/32901', methods=['GET'])

def weather(zip_code):

#base URL of the weather website
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
#API key retrieved from the weather website
    #API_KEY = "6f8628fda32712e5b77d10cd5672d8e4"
    API_KEY = os.environ["API_KEY"]
#complete URL to be used
    URL = base_url + "zip=" + zip_code + "&APPID=" + API_KEY
#http request
    r = requests.get(URL)
#getting the responce in json format
    data = r.json()
#decoupling the json data to retrieve needed variables  
    mainy = data['main']
    temperature = mainy['temp']
    temperature = str(round((temperature - 273.15) * 1.8 + 32)) + 'F'
    report = data['weather']
#converting needed response to json format   
    list_data = {
        "city": data['name'],
        "temp": temperature,
        "humidity": mainy['humidity'],
        "pressure": mainy['pressure'],
        "weather_report": report[0]['description']
    }

#returning the resutling json to be displayed in a web browser
    return list_data
    
#other possibilities of display
    #return f"Current weather for {}", city 
    #return f"Current weather for {} is {}F with {} humidity of {} and pressure {}", city, temperature, climate, humidity, pressure
    #return f"The current weather for {city} is Temperature: {temperature}F, Humidity: {humidity}, Pressure: {pressure}, with {climate} "
    
        
#provide port and other parameters
if __name__ == "__main__":   
    app.run(host="0.0.0.0", debug=True)
