from django.conf.urls import url
from . import views

app_name = 'calendarApp'
urlpatterns = [
    url(r'^index/$', views.index, name=''),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
]