from flask import Flask, render_template, request
import requests

app = Flask(_name_)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        api_key = '**************************' # replace this with your Visual Crossing Corporation Weather API key
        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={api_key}&contentType=json'
        response = requests.get(url)
        weather_data = response.json()

    return render_template('index.html', weather_data=weather_data)

if _name_ == '_main_':
    app.run(debug=True)
