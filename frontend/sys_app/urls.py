from django.urls import path
from . import views


app_name = 'sys_app'
urlpatterns =[
    path('',views.homepage, name='homepage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('conteudo/',views.conteudo, name='conteudo'),
    path('materia/', views.materia, name='materia'),
    path('materia/atividade/',views.atividade, name='atividade'),
    path('materia/cadastrar/', views.cadastrasMateria, name='cadastrasMateria'),
    path('perfil/',views.perfil, name='perfil'),
]