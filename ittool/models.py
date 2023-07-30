from django.db import models


class Plugin(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    icon = models.ImageField(upload_to="icons/%Y/%m/%d/",
                             blank=True, verbose_name='Иконка')
    dev_name = models.CharField(
        max_length=255, verbose_name='Ник разработчика')
    date_added = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата добавления')
    slug = models.SlugField(unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Плагин'
        verbose_name_plural = 'Плагины'
        ordering = ['date_added', 'name']

    def __str__(self):
        return self.name
