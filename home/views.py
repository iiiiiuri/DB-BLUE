from django.shortcuts import render

def home(request):

    return render(request, 'home\home.html')



def login(request):

    return render(request, 'login\login.html')