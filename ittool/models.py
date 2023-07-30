from django.db import models


class Plugin(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    icon = models.ImageField(upload_to="icons/%Y/%m/%d/",
                             blank=True, verbose_name='Icon')
    description = models.TextField(verbose_name='Description')
    dev_name = models.CharField(
        max_length=255, verbose_name='Developer name')
    date_added = models.DateTimeField(
        auto_now_add=True, verbose_name='Date added')
    version = models.CharField(max_length=10, verbose_name='Version')
    slug = models.SlugField(unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Plugin'
        verbose_name_plural = 'Plugins'
        ordering = ['date_added', 'name']

    def __str__(self):
        return self.name
