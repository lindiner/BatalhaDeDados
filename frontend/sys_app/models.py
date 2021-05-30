from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    name = models.CharField("Nome da Questão", max_length=200)
    tags = models.JSONField("Tipos de questões",default=None,null=True)
    # aqui tem até a resposta correta
    responses = models.JSONField("Respostas",default=None,null=True)
class Plano(models.Model):
    name = models.CharField("Nome do Modelo",max_length=200)
    questions = models.ManyToManyField(Question)
    
class Turma(models.Model):
    name = models.CharField("Nome da matéria",max_length=200)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ProfessorResponável")
    students = models.ManyToManyField(User,blank=True)
    plans = models.ManyToManyField(Plano)





