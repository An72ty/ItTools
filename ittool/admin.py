from django.contrib import admin
from .models import Plugin


class PluginAdmin(admin.ModelAdmin):
    search_fields = ('name', 'dev_name')
    list_display = ('name', 'dev_name', 'slug', 'icon', 'date_added')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    


admin.site.register(Plugin, PluginAdmin)
