from django.shortcuts import render
import requests

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=16d8f8042bea161885dffd2d111fa5af'
    city = 'Las Vegas'
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    context = {'weather' : weather}
    return render(request, 'weather/index.html', context) #returns the index.html template