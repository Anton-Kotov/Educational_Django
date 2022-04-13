from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):


    abc = "abcdefghyjklmnopqrstyvwxyz"
    characters = list(abc)
    length = int(request.GET.get('length'))
    thepassword = ''

    if request.GET.get('uppercase'):
        characters.extend(abc.upper())

    if request.GET.get('special'):
        characters.extend('!@#$%^&*()-+=')

    if request.GET.get('numbers'):
        characters.extend('1234567890')

    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, 'generator/password.html', {'password': thepassword})