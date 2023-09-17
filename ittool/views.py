from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Plugin, ItToolsVersion
from .utils import menu, str_queryset_to_list, list_to_queryset


# def index(request):
#     context = {'menu': menu, 'page_selected': -1}
#     return render(request, 'ittool/index.html', context)


class Index(TemplateView):
    template_name = 'ittool/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['menu'] = menu
        context['page_selected'] = -1

        return context


# def plugins(request):
#     plugins = Plugin.objects.all()
#     if request.method == 'GET':
#         plugins_filter = request.GET.get('plugin_or_dev_name')
#         name_filter = request.GET.get('name_filter')
#         date_filter = request.GET.get('date_filter')
#         plugins_list = []
#         if plugins_filter:
#             for plugin in Plugin.objects.all():
#                 if plugins_filter.lower() in plugin.name.lower():
#                     plugins_list.append(plugin)
#                 elif plugins_filter.lower() in plugin.dev_name.lower():
#                     plugins_list.append(plugin)
#             plugins = list_to_queryset(Plugin, plugins_list)

#         if request.GET.get('past_plugins'):
#             past_plugins = list_to_queryset(
#                 Plugin, str_queryset_to_list(Plugin, request.GET.get('past_plugins')))
#             if name_filter:
#                 plugins = past_plugins.order_by(name_filter)
#             if date_filter:
#                 plugins = past_plugins.order_by(date_filter)

#     context = {'menu': menu, 'page_selected': 1, 'plugins': plugins}
#     return render(request, 'ittool/plugins.html', context)


class Plugins(ListView):
    model = Plugin
    template_name = 'ittool/plugins.html'
    context_object_name = 'plugins'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['menu'] = menu
        context['page_selected'] = 1

        return context

    def get_queryset(self):
        plugins = Plugin.objects.all()
        if self.request.method == 'GET':
            plugins_filter = self.request.GET.get('plugin_or_dev_name')
            name_filter = self.request.GET.get('name_filter')
            date_filter = self.request.GET.get('date_filter')
            plugins_list = []
            if plugins_filter:
                for plugin in Plugin.objects.all():
                    if plugins_filter.lower() in plugin.name.lower():
                        plugins_list.append(plugin)
                    elif plugins_filter.lower() in plugin.dev_name.lower():
                        plugins_list.append(plugin)
                plugins = list_to_queryset(Plugin, plugins_list)

            if self.request.GET.get('past_plugins'):
                past_plugins = list_to_queryset(
                    Plugin, str_queryset_to_list(Plugin, self.request.GET.get('past_plugins')))
                if name_filter:
                    plugins = past_plugins.order_by(name_filter)
                if date_filter:
                    plugins = past_plugins.order_by(date_filter)

        return plugins


# def eternal_arts(request):
#     context = {'menu': menu, 'page_selected': 2}
#     return render(request, 'ittool/eternal_arts.html', context)


class EternalArts(TemplateView):
    template_name = 'ittool/eternal_arts.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['menu'] = menu
        context['page_selected'] = 2

        return context


# def plugin(request, slug):
#     plugin = get_object_or_404(Plugin, slug=slug)

#     context = {'menu': menu, 'page_selected': -1, 'plugin': plugin}
#     return render(request, 'ittool/plugin.html', context)


class ShowPlugin(DetailView):
    model = Plugin
    context_object_name = 'plugin'
    template_name = 'ittool/plugin.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['menu'] = menu
        context['page_selected'] = -1

        return context


# def downloads(request):
#     versions = ItToolsVersion.objects.all()

#     context = {'menu': menu, 'page_selected': 0, 'versions': versions}
#     return render(request, 'ittool/downloads.html', context)


class Downloads(ListView):
    model = ItToolsVersion
    template_name = 'ittool/downloads.html'
    context_object_name = 'versions'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['menu'] = menu
        context['page_selected'] = 0

        return context

    def get_queryset(self):
        return ItToolsVersion.objects.all()


# def about(request):
#     context = {'menu': menu, 'page_selected': 3}
#     return render(request, 'ittool/about.html', context)


class About(TemplateView):
    template_name = 'ittool/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['menu'] = menu
        context['page_selected'] = 3

        return context
