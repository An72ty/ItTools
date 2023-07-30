from django.shortcuts import render
from .models import Plugin


def index(request):
    return render(request, 'ittool/index.html')


def plugins(request):
    plugins = Plugin.objects.all()
    
    context = {'plugins': plugins}
    return render(request, 'ittool/plugins.html', context)
