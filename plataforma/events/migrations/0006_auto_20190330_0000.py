# Generated by Django 2.1.7 on 2019-03-30 05:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20190328_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
