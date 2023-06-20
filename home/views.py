from django.shortcuts import render
from .models import contas

def home(request):

    return render(request, 'home\home.html')



def login(request):

    return render(request, 'login\login.html')

def signup(request):
    cadastro = contas()
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    senha = request.POST.get('pass')
    usuario = request.POST.get('user')
    email = request.POST.get('email')
    cadastro.save()
    return render (request, 'signup\signup.html')