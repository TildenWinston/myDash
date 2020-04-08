from django.shortcuts import render, redirect
import requests, json
from .models import City, Zipcode
from .forms import CityForm, ZipForm
from . import views

# Comment

def index(request):
    # print(request)
    url = 'http://api.openweathermap.org/data/2.5/forecast?zip={}&units=imperial&appid=16d8f8042bea161885dffd2d111fa5af'
    #cities = City.objects.all()
    zips = Zipcode.objects.all()
    # print(zips[1].user)
    print(request.user)

    if request.method == 'POST':
        #print(request.user)
        #print(request.POST['zip'])

        model = Zipcode()
        model.zip = request.POST['zip']
        #print(model.zip)
        model.zip = model.zip
        model.user = request.user
        model.save()


        # model.user = 'admin'
        # model.save()

        # data = Zipcode(user=request.user)
        # print(data)
        # zipform = ZipForm(request.POST, instance=data)
        # #data.save()
        # zipform
        # print(zipform)
        # zipform.save()
        
        # zipform = ZipForm(request.POST)
        # print(zipform)
        # zipform.save()
        return redirect('weather:index')    

    zipform = ZipForm()

    weather_data = []

    for zip in zips:
        if(zip.user == request.user):
            print(zip)
            city_weather = requests.get(url.format(zip)).json() #request the API data and convert the JSON to Python data types
            # print(json.dumps(city_weather, indent = 4, sort_keys=True))

            weather = {
                'city' : zip,
                'temperature' : city_weather['list'][0]['main']['temp'],
                'description' : city_weather['list'][0]['weather'][0]['description'],
                'icon' : city_weather['list'][0]['weather'][0]['icon']
            }

            weather_data.append(weather)

    context = {'weather_data' : weather_data, 'zipform' : zipform}
    return render(request, 'weather/index.html', context) #returns the index.html template
