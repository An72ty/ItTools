from django.urls import path
from .views import index


app_name = 'ittool'
urlpatterns = [
    path('', index, name='index')
]
