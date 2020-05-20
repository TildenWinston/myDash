from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class MainPageView(TemplateView):
    template_name = 'dashboard.html'


@login_required(login_url='/')
def index(response):
    return render(response, 'dashboard.html')