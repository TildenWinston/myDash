from django.shortcuts import render, redirect
import requests, json
from .models import City, Zipcode
from .forms import CityForm, ZipForm
from . import views
from django.views.decorators.clickjacking import xframe_options_exempt

# https://www.digitalocean.com/community/tutorials/how-to-build-a-weather-app-in-django#creating-the-form


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
        #model.zip = model.zip
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
            print(json.dumps(city_weather, indent = 4, sort_keys=True))

            if (city_weather["cod"] == "200"):
                weather = {
                    'city' : zip,
                    'temperature' : city_weather['list'][0]['main']['temp'],
                    'description' : city_weather['list'][0]['weather'][0]['description'],
                    'icon' : city_weather['list'][0]['weather'][0]['icon']
                }
            
            else:
                weather = {
                    'city' : zip,
                    'temperature' : 404,
                    'description' : "Bad Zipcode, delete and try again with a valid zipcode.",
                }


            weather_data.append(weather)

    context = {'weather_data' : weather_data, 'zipform' : zipform}
    return render(request, 'weather/index.html', context) #returns the index.html template

def delete(request, zip):
    zips = Zipcode.objects.all()
    print(zip)
    Zipcode.objects.filter(zip=zip, user=request.user).delete()
    return redirect('weather:index') 
"""     for zipobj in zips:
        if(zipobj.user == request.user):
            if(zipobj.zip == zip):
                print("Match")
                Zipcode.objects.delete(zipobj) """
    
    


@xframe_options_exempt
def dashapp(request):
    # print(request)
    url = 'http://api.openweathermap.org/data/2.5/forecast?zip={}&units=imperial&appid=16d8f8042bea161885dffd2d111fa5af'
    #cities = City.objects.all()
    zips = Zipcode.objects.all()

    weather_data = []

    for zip in zips:
        if(zip.user == request.user):
            print(zip)
            city_weather = requests.get(url.format(zip)).json() #request the API data and convert the JSON to Python data types
            # print(json.dumps(city_weather, indent = 4, sort_keys=True))

            if (city_weather["cod"] == "200"):
                weather = {
                    'city' : zip,
                    'temperature' : city_weather['list'][0]['main']['temp'],
                    'description' : city_weather['list'][0]['weather'][0]['description'],
                    'icon' : city_weather['list'][0]['weather'][0]['icon']
                }
            
            else:
                weather = {
                    'city' : zip,
                    'temperature' : 404,
                    'description' : "Bad Zipcode, delete and try again with a valid zipcode.",
                }


            weather_data.append(weather)

    context = {'weather_data' : weather_data, }
    return render(request, 'weather/dashapp.html', context) #returns the index.html template

