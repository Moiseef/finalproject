# Generated by Django 4.0.3 on 2023-03-14 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0006_about_articl_about_slide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title_contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('full_text', models.TextField(verbose_name='Articl')),
            ],
        ),
    ]
