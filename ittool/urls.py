from django.urls import path
from .views import index, plugins


app_name = 'ittool'
urlpatterns = [
    path('', index, name='index'),
    path('plugins/', plugins, name='plugins')
]
