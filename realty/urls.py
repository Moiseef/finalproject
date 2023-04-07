from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name= "logout"),
    path('create/', views.create_project, name='create'),
    path("about/", views.about, name='about'),
    path("objects/", views.realty, name='realty'),
    path("contact/", views.contact, name='contact'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('realty/<int:pk>/', views.RealtyViews.as_view(), name="views")
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)