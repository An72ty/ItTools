from django.shortcuts import render
from .models import Plugin


menu = [{'title': 'Download', 'url': 'ittool:download'},
        {'title': 'Plugins', 'url': 'ittool:plugins', },
        {'title': 'Eternal Arts', 'url': 'ittool:eternal-arts', },
        {'title': 'About', 'url': 'ittool:about'}
        ]


def index(request):
    context = {'menu': menu, 'page_selected': -1}
    return render(request, 'ittool/index.html', context)


def plugins(request):
    plugins = Plugin.objects.all()

    context = {'menu': menu, 'page_selected': 1, 'plugins': plugins}
    return render(request, 'ittool/plugins.html', context)
