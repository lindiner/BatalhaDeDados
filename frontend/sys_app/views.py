from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse

# Create your views here.


def homepage(request):
    return render(request, "landing.html")


def dashboard(request):
    group = [str(x) for x in request.user.groups.all()]

    if 'professor' in group:
        return render(request, "dashboard_professor.html", {"group": group[0],"user": request.user})
    if 'escola' in group:
        return render(request, "dashboard_escola.html", {"group": group[0],"user": request.user})
    if 'aluno' in group:
        return render(request, "dashboard_aluno.html", {"group": group[0],"user": request.user})
    
    logout(request)
    # raise Http404("Você não tem permissão de acesso")
    return HttpResponseRedirect(reverse('authapp:login'))

def conteudo(request):
    cards = [
        {
            "name": "Questionário 1",
            "desc": "Destinado a soma",
            "ap": "80"
        },
        {
            "name": "Questionário 2",
            "desc": "Destinado a subtração",
            "ap": "60"
        },
        {
            "name": "Questionário 4",
            "desc": "Destinado a multiplicação",
            "ap": "34"
        }
    ]

    cardsRec = [
        {
            "name": "Questionário 4",
            "desc": "Destinado a soma",
            "ap": "100"
        },
        {
            "name": "Questionário 32",
            "desc": "Destinado a subtração",
            "ap": "80"
        },
        {
            "name": "Questionário 51",
            "desc": "Destinado a multiplicação",
            "ap": "96"
        }
    ]
    return render(request, "dashboard_conteudo.html", {"cards": cards,"cardsRec":cardsRec})