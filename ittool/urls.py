from django.urls import path
from .views import index, plugins


app_name = 'ittool'
urlpatterns = [
    path('', index, name='index'),
    path('download/', index, name='download'),
    path('plugins/', plugins, name='plugins'),
    path('eternal-arts/', index, name='eternal-arts'),
    path('about/', index, name='about'),
]
