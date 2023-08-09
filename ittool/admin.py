from django.contrib import admin
from .models import Plugin, ItToolsVersion


class PluginAdmin(admin.ModelAdmin):
    search_fields = ('name', 'dev_name')
    list_display = ('name', 'dev_name', 'version',
                    'slug', 'icon', 'date_added')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('dev_name', 'date_added')


class ItToolsVersionAdmin(admin.ModelAdmin):
    search_fields = ('version', 'version_type')
    list_display = ('version', 'name', 'version_type', 'date_added')
    list_display_links = ('version',)
    list_filter = ('version_type', 'date_added')


admin.site.register(Plugin, PluginAdmin)
admin.site.register(ItToolsVersion, ItToolsVersionAdmin)
