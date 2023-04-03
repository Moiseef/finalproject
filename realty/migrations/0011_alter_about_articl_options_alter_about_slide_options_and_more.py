# Generated by Django 4.0.3 on 2023-03-18 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0010_contact_form_alter_call_us_link_fph_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about_articl',
            options={'verbose_name': 'About aricl', 'verbose_name_plural': 'About articles'},
        ),
        migrations.AlterModelOptions(
            name='about_slide',
            options={'verbose_name': 'About slide', 'verbose_name_plural': 'About slides'},
        ),
        migrations.AlterModelOptions(
            name='call_us',
            options={'verbose_name': 'Call us block', 'verbose_name_plural': 'Call us blocks'},
        ),
        migrations.AlterModelOptions(
            name='contact_form',
            options={'verbose_name': 'Contact form', 'verbose_name_plural': 'Contact forms'},
        ),
        migrations.AlterModelOptions(
            name='email_us',
            options={'verbose_name': 'Email us block', 'verbose_name_plural': 'Email us blocks'},
        ),
        migrations.AlterModelOptions(
            name='home_articl',
            options={'verbose_name': 'Home title', 'verbose_name_plural': 'Home titles'},
        ),
        migrations.AlterModelOptions(
            name='home_slide',
            options={'verbose_name': 'Home slides'},
        ),
        migrations.AlterModelOptions(
            name='logo',
            options={'verbose_name': 'Logo', 'verbose_name_plural': 'Logos'},
        ),
        migrations.AlterModelOptions(
            name='social_us',
            options={'verbose_name': 'Social us block', 'verbose_name_plural': 'Social us blocks'},
        ),
        migrations.AlterModelOptions(
            name='title_contact',
            options={'verbose_name': 'Contact title', 'verbose_name_plural': 'Contact titles'},
        ),
    ]
