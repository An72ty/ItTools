from django.db import models
from django.urls import reverse


class Plugin(models.Model):
    name = models.CharField(max_length=15, verbose_name='Name')
    icon = models.ImageField(upload_to="icons/%Y/%m/%d/",
                             blank=True, verbose_name='Icon')
    description = models.TextField(verbose_name='Description', max_length=180)
    dev_name = models.CharField(
        max_length=15, verbose_name='Developer name')
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

    def get_absolute_url(self):
        return reverse('ittool:plugin', kwargs={'slug': self.slug})


class ItToolsVersion(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    version = models.CharField(max_length=10, verbose_name='Version')
    version_type = models.CharField(max_length=20, verbose_name='Version Type')
    file = models.FileField(upload_to="files/%Y/%m/%d/", verbose_name='File')
    date_added = models.DateTimeField(
        auto_now_add=True, verbose_name='Date added')

    class Meta:
        verbose_name = 'ITTOOLS Version'
        verbose_name_plural = 'ITTOOLS Versions'
        ordering = ['-version']
