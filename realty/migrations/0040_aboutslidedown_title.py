# Generated by Django 4.1.7 on 2023-04-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0039_aboutslidedown'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutslidedown',
            name='title',
            field=models.CharField(default='Title', max_length=50, verbose_name='Title'),
        ),
    ]
