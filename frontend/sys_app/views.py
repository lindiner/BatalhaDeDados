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
    group = [str(x) for x in request.user.groups.all()]
    cardM = [
        {
            "name": "Matematica",
            "desc": "e suas tecnologias",
            "Andamento": "1"
        }

    ]
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
    return render(request, "dashboard_conteudo.html", {"cardM": cardM,"cards": cards,"cardsRec":cardsRec, 'textButton':"entrar","group": group[0],"user": request.user})

def materia(request):
    group = [str(x) for x in request.user.groups.all()]
    cards = [
        {
            "name": "Matematica",
            "desc": "e suas tecnologias",
            "ap": "80"
        },
        {
            "name": "Portugues",
            "desc": "e suas tecnologias",
            "ap": "60"
        },
       
    ]
    cardsENEM = [
        {
            "name": "Ciências da Natureza e suas Tecnologias",
            "desc": "Biologia, Fisica, Quimica",
            "ap": "50"
        },
        {
            "name": "Ciências Humanas e suas Tecnologias",
            "desc": "Historia, Geografia, Sociologia e Filosofia",
            "ap": "55"
        },
        {
            "name": "Matemática e suas Tecnologias",
            "desc": "Matematica",
            "ap": "65"
        },
        {
            "name": "Linguagens, suas Tecnologias e Redação",
            "desc": "Matematica",
            "ap": "76"
        }
    ]
    cardsRec = [
        {
            "name": "Algrebra linear",
            "desc": "Álgebra linear é um ramo da matemática que surgiu do estudo detalhado de sistemas de equações lineares, sejam elas algébricas ou diferenciais",
            "ap": "50"
        },
        {
            "name": "Numeros reais",
            "desc": "Chamamos de Números Reais o conjunto de elementos, representado pela letra maiúscula R, que inclui os",
            "ap": "55"
        },
        {
            "name": "Conjuntos",
            "desc": "Na matemática, um conjunto é uma coleção de elementos.",
            "ap": "65"
        }
    ]



    return render(request, "materiaAluno.html",  {"cards": cards,"cardsENEM":cardsENEM , "cardsRec":cardsRec, 'textButton':"Entrar","group": group[0],"user": request.user} )

def atividade(request):
    group = [str(x) for x in request.user.groups.all()]
    return render(request, "cadastrarQuestionario.html",{"group": group[0],"user": request.user})

def cadastrasMateria(request):
    group = [str(x) for x in request.user.groups.all()]
    return render(request, "materiaProfessor.html",{"group": group[0],"user": request.user})

def perfil(request):
    group = [str(x) for x in request.user.groups.all()]
    return render(request, "profile.html",{"group": group[0],"user": request.user})
