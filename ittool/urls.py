from django.urls import path
from .views import Index, Plugins, EternalArts, ShowPlugin, Downloads, About


app_name = 'ittool'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('downloads/', Downloads.as_view(), name='downloads'),
    path('plugins/', Plugins.as_view(), name='plugins'),
    path('eternal-arts/', EternalArts.as_view(), name='eternal-arts'),
    path('about/', About.as_view(), name='about'),
    path('plugin/<slug>/', ShowPlugin.as_view(), name='plugin')
]
