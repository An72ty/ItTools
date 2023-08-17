from django.urls import path
from .views import index, plugins, eternal_arts, plugin, downloads, about


app_name = 'ittool'
urlpatterns = [
    path('', index, name='index'),
    path('downloads/', downloads, name='downloads'),
    path('plugins/', plugins, name='plugins'),
    path('eternal-arts/', eternal_arts, name='eternal-arts'),
    path('about/', about, name='about'),
    path('plugin/<slug>/', plugin, name='plugin')
]
