from django.urls import path
from .views import index, plugins, eternal_arts, plugin


app_name = 'ittool'
urlpatterns = [
    path('', index, name='index'),
    path('downloads/', index, name='downloads'),
    path('plugins/', plugins, name='plugins'),
    path('eternal-arts/', eternal_arts, name='eternal-arts'),
    path('about/', index, name='about'),
    path('plugin/<slug>/', plugin, name='plugin')
]
