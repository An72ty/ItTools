from django.urls import path
from .views import index, plugins


app_name = 'ittool'
urlpatterns = [
    path('', index, name='index'),
    path('downloads/', index, name='downloads'),
    path('plugins/', plugins, name='plugins'),
    path('eternal-arts/', index, name='eternal-arts'),
    path('about/', index, name='about'),
]
