from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product
from .models import Image
from django.forms import ModelForm

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user        

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'full_text', 'price',)


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
    
    
