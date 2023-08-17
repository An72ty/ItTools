from django.shortcuts import render
from .models import Plugin, ItToolsVersion


menu = [{'title': 'Downloads', 'url': 'ittool:downloads', 'page_number': 0},
        {'title': 'Plugins', 'url': 'ittool:plugins', 'page_number': 1},
        {'title': 'Eternal Arts', 'url': 'ittool:eternal-arts', 'page_number': 2},
        {'title': 'About', 'url': 'ittool:about', 'page_number': 3}
        ]


def list_to_queryset(model, data):
    from django.db.models.base import ModelBase

    if not isinstance(model, ModelBase):
        raise ValueError(
            "%s must be Model" % model
        )
    if not isinstance(data, list):
        raise ValueError(
            "%s must be List Object" % data
        )

    pk_list = [obj.pk for obj in data]
    return model.objects.filter(pk__in=pk_list)


def str_queryset_to_list(model, data) -> list:
    from django.db.models.base import ModelBase

    if not isinstance(model, ModelBase):
        raise ValueError(
            "%s must be Model" % model
        )
    if not isinstance(data, str):
        raise ValueError(
            "%s must be Str Object" % data
        )

    raw_list = data.split('[')
    raw_element = raw_list[1]
    raw_list_2 = raw_element.split(']')
    raw_element_2 = raw_list_2[0]
    raw_list_3 = raw_element_2.split(', ')

    model_list = []
    for model_str in raw_list_3:
        el = model_str.split(' ')
        try:
            e = el[1]
        except IndexError:
            return []
        el2 = e.split('>')
        model_name = el2[0]
        model_list.append(model.objects.get(name=model_name))

    return model_list


def index(request):
    context = {'menu': menu, 'page_selected': -1}
    return render(request, 'ittool/index.html', context)


def plugins(request):
    plugins = Plugin.objects.all()
    if request.method == 'GET':
        plugins_filter = request.GET.get('plugin_or_dev_name')
        name_filter = request.GET.get('name_filter')
        date_filter = request.GET.get('date_filter')
        plugins_list = []
        if plugins_filter:
            for plugin in Plugin.objects.all():
                if plugins_filter.lower() in plugin.name.lower():
                    plugins_list.append(plugin)
                elif plugins_filter.lower() in plugin.dev_name.lower():
                    plugins_list.append(plugin)
            plugins = list_to_queryset(Plugin, plugins_list)

        if request.GET.get('past_plugins'):
            past_plugins = list_to_queryset(
                Plugin, str_queryset_to_list(Plugin, request.GET.get('past_plugins')))
            if name_filter:
                plugins = past_plugins.order_by(name_filter)
            if date_filter:
                plugins = past_plugins.order_by(date_filter)

    context = {'menu': menu, 'page_selected': 1, 'plugins': plugins}
    return render(request, 'ittool/plugins.html', context)


def eternal_arts(request):
    context = {'menu': menu, 'page_selected': 2}
    return render(request, 'ittool/eternal_arts.html', context)


def plugin(request, slug):
    context = {'menu': menu, 'page_selected': -1}
    return render(request, 'ittool/index.html', context)


def downloads(request):
    versions = ItToolsVersion.objects.all()

    context = {'menu': menu, 'page_selected': 0, 'versions': versions}
    return render(request, 'ittool/downloads.html', context)


def about(request):
    context = {'menu': menu, 'page_selected': 3}
    return render(request, 'ittool/about.html', context)
