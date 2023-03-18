from django.db import models

# Create your models here.
class Home_articl(models.Model):
    title = models.CharField('Title', max_length=50)
    mutetext = models.CharField('Mute', max_length=50)  
    full_text = models.TextField('Articl')
    venue_image = models.ImageField('Image', null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

class Home_slide(models.Model):
    title = models.CharField('Title', max_length=50)
    text_slide = models.CharField('Text', max_length=250)
    link_text = models.CharField('Button', default='Link', max_length=50) 
    link_slide = models.CharField('Link', max_length=50)    
    slide_image = models.ImageField('Image', null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title    
    
class Logo(models.Model):
    title = models.CharField('Title', max_length=50, default='logo')
    logo_image = models.ImageField('Image', null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title   
    
class About_articl(models.Model):
    title = models.CharField('Title', max_length=50)
    mutetext = models.CharField('Mute', max_length=50)  
    full_text = models.TextField('Articl')
    venue_image = models.ImageField('Image', null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

class About_slide(models.Model):
    title = models.CharField('Title', max_length=50)
    text_slide = models.CharField('Text', max_length=250)
    link_text = models.CharField('Button', default='Link', max_length=50) 
    link_slide = models.CharField('Link', max_length=50)    
    slide_image = models.ImageField('Image', null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title    

class Title_contact(models.Model):
    title = models.CharField('Title', max_length=50)
    full_text = models.TextField('Articl')                

    def __str__(self):
        return self.title    