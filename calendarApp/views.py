from datetime import datetime, timedelta, date
import calendar
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe

from django.http import HttpResponseRedirect

from .models import *
from .utils import Calendar
from .forms import EventForm

# https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html

def index(request):
    return HttpResponse('Test')


class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendarApp/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        user = self.request.user
        cal = Calendar(d.year, d.month, user)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)

        # Event.objects
        # context['event_list'] = Event(user = self.request.user)
        # print(self.request.user)
        return context



def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        model = Event()
        model.user = request.user
        model.title = request.POST['title']
        model.description = request.POST['description']
        model.start_time = request.POST['start_time']
        model.end_time = request.POST['end_time']

        model.save() 
        return HttpResponseRedirect(reverse('calendarApp:calendar'))
    
    return render(request, 'calendarApp/event.html', {'form': form})