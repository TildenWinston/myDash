from django.shortcuts import render
import requests, json
from .models import City, Zipcode
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q={}&units=imperial&appid=16d8f8042bea161885dffd2d111fa5af'
    cities = City.objects.all()

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []

    for city in cities:
        # print(city)
        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
        print(json.dumps(city_weather, indent = 4, sort_keys=True))

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/index.html', context) #returns the index.html template