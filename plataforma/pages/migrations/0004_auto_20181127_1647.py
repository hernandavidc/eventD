# Generated by Django 2.1 on 2018-11-27 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20181127_1646'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order', '-id', 'title'], 'verbose_name': 'entrada', 'verbose_name_plural': 'entradas'},
        ),
    ]
