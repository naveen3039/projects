from flask import Flask ,request
import requests

app = Flask(__name__)

@app.route('/city')
def search_city():
    API_KEY = 'f7357d8a576a6f644b94d70e21e116b2'  # initialize your key here
    city = request.args.get('london')  # city name passed as argument
    


    # call API and convert response into Python dictionary
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
    response = requests.get(url).json()
    
    # error like unknown city name, inavalid api key
    if response.get('cod') != 200:
        message = response.get('message', '')
        return f'Error getting temperature for {city.title()}. Error message = {message}'
    
    # get current temperature and convert it into Celsius
    current_temperature = response.get('main', {}).get('temp')
    if current_temperature:
        current_temperature_celsius = round(current_temperature - 273.15, 2)
        return f'Current temperature of {city.title()} is {current_temperature_celsius} &#8451;'
    else:
        return f'Error getting temperature for {city.title()}'



if __name__== "__main__":
    app.run(debug=True,port=5004)