from django.urls import path,include
from . import views

app_name = 'authapp'

urlpatterns  = [
    path('login/', views.login, name='login'),
]