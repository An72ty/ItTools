# Generated by Django 4.2.3 on 2023-08-09 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ittool', '0006_alter_ittoolsversion_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ittoolsversion',
            options={'ordering': ['-version'], 'verbose_name': 'ITTOOLS Version', 'verbose_name_plural': 'ITTOOLS Versions'},
        ),
    ]
