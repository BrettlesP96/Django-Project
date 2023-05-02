from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('show_user/', views.show_user, name='show_user'),
    path('authenticate/', views.authenticate_user, name='authenticate'),
]
