from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.


def home(request):
    return render(request, 'generator_app/home.html')


def password(request):
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend([x.upper() for x in characters])
    if request.GET.get('numbers'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('characters'):
        characters.extend(list('0123456789'))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    print(request)
    return render(request, 'generator_app/password.html', {'password': thepassword})
