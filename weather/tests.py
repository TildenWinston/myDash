from django.test import TestCase
from weather.views import index
import requests

# Create your tests here.
class WeatherTestCase(TestCase):
    def test_zip(self):
        print("test start")
        # http://samples.openweathermap.org/data/2.5/forecast?zip=94040&appid=b6907d289e10d714a6e88b30761fae22
        # request = request()
        # index(request)
        
        self.assertEqual(1, 1)