from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login as authLogin, logout as authLogout
from django.urls import reverse

# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('sys_app:dashboard'))

    if request.method == 'POST':
        print(request.POST)
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            authLogin(request, user)
            return HttpResponseRedirect(reverse('sys_app:dashboard'))

    return render(request,'login.html',{"teste": "ALLLOW"})

def register(request):
    # tem??
    pass

def logout(request):
    authLogout(request)
    pass