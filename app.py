import requests
import configparser
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def weather_dashboard():
    return render_template('home.html')

    app.route('/results')
    def render_results():
        city_name = request.form['city name']
        return "city name:" + city_name

        if __name__ == '__main__':
            app.run()

def get_api_key():
    config = configparser.Configparser
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather_results(city_name, api_key):
    api_url ="api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)
    r = requests.get(api_url)
    return r.json()

    print(get_weather_results("London", get_api_key()))