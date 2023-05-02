from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Band'

urlpatterns = [
    path('', views.home, name='home'),
    path('discography/', views.discography, name='discography'),
    path('about.html', views.about, name='about'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
