from django.contrib import admin
from .models import Turma,Plano,Question
# Register your models here.

class TurmaAdmin(admin.ModelAdmin):
    pass
class PlanosAdmin(admin.ModelAdmin):
    pass
class QuestionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Turma,TurmaAdmin)
admin.site.register(Plano,PlanosAdmin)
admin.site.register(Question,QuestionAdmin)