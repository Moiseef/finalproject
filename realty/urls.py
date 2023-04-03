from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path("logout/", views.logout_request, name= "logout"),
    path("create/", views.create_project, name='create')
]