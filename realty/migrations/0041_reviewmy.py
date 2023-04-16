# Generated by Django 4.1.7 on 2023-04-13 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0040_aboutslidedown_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewMy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('full_text', models.TextField(verbose_name='Articl')),
                ('image_avatar', models.ImageField(blank=True, default='/media/images/images/avatar.jpg', max_length=500, null=True, upload_to='images/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
