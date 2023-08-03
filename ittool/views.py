from django.shortcuts import render
from .models import Plugin


menu = [{'title': 'Download', 'url': 'ittool:download', 'page_number': 0},
        {'title': 'Plugins', 'url': 'ittool:plugins', 'page_number': 1},
        {'title': 'Eternal Arts', 'url': 'ittool:eternal-arts', 'page_number': 2},
        {'title': 'About', 'url': 'ittool:about', 'page_number': 3}
        ]


def index(request):
    context = {'menu': menu, 'page_selected': -1}
    return render(request, 'ittool/index.html', context)


def plugins(request):
    plugins = Plugin.objects.all()

    context = {'menu': menu, 'page_selected': 1, 'plugins': plugins}
    return render(request, 'ittool/plugins.html', context)
