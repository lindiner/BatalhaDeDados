from django.urls import path
from . import views


app_name = 'sys_app'
urlpatterns =[
    path('',views.homepage, name='homepage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('conteudo/',views.conteudo, name='conteudo'),
]