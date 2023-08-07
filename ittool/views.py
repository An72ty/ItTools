from django.shortcuts import render
from .models import Plugin


menu = [{'title': 'Downloads', 'url': 'ittool:downloads', 'page_number': 0},
        {'title': 'Plugins', 'url': 'ittool:plugins', 'page_number': 1},
        {'title': 'Eternal Arts', 'url': 'ittool:eternal-arts', 'page_number': 2},
        {'title': 'About', 'url': 'ittool:about', 'page_number': 3}
        ]


def index(request):
    context = {'menu': menu, 'page_selected': -1}
    return render(request, 'ittool/index.html', context)


def plugins(request):
    plugins = Plugin.objects.all()
    if request.method == 'GET':
        plugins_filter = request.GET.get('plugin_or_dev_name')
        name_filter = request.GET.get('name_filter')
        date_filter = request.GET.get('date_filter')
        if plugins_filter:
            plugins = []
            for plugin in Plugin.objects.all():
                if plugins_filter.lower() in plugin.name.lower():
                    plugins.append(plugin)
                elif plugins_filter.lower() in plugin.dev_name.lower():
                    plugins.append(plugin)
            plugins.sort()
        if name_filter:
            plugins = Plugin.objects.order_by(name_filter)
        if date_filter:
            plugins = Plugin.objects.order_by(date_filter)

    context = {'menu': menu, 'page_selected': 1, 'plugins': plugins}
    return render(request, 'ittool/plugins.html', context)


def eternal_arts(request):
    context = {'menu': menu, 'page_selected': 2}
    return render(request, 'ittool/eternal_arts.html', context)


def plugin(request, slug):
    context = {'menu': menu}
    return render(request, 'ittool/index.html', context)
