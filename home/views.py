from django.shortcuts import render
from .models import contas


def home(request):

    return render(request, 'home\home.html')



def login(request):

    return render(request, 'login\login.html')

def signup(request):
    return render (request, 'signup\signup.html')

def cadastrar(request):
    cadastro = contas()
    cadastro.nome = request.POST.get('nome')
    cadastro.sobrenome = request.POST.get('sobrenome')
    cadastro.senha = request.POST.get('pass')
    cadastro.user = request.POST.get('user')
    cadastro.email = request.POST.get('email')
    cadastro.save()
    return render (request, 'home\home.html')



