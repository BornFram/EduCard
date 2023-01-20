from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
from .models import *
from .logics import *

config = json.load(open('main/config/config.json'))


def home(request):

    context={
        'title': 'EduCard',
        'clas': Classes.objects.all(),
        'popItems': Items.objects.filter(raiting__gte=config.get('mpr'))
    }
    return render(request,'main/Home.html',context=context)


def catalogURLregen(request):
    return redirect('')
def catalog(request,catalogPath):
    catalogPath = catalogPath.split('/')
    print('CAT PATH: ',catalogPath)
    returnHtml = 'main/Catalog.html'
    li=[]

    match len(catalogPath):
        case 1:
            print('='*10,1)
            li = Subjects.objects.filter(
                clas=Classes.objects.get(name=catalogPath[0]).id)
            print('='*10,1)
        case 2:
            print('='*10,2)
            li = Themes.objects.filter(
                subject=Subjects.objects.get(name=catalogPath[1]).id)
            print('=' * 10, 2)
        case 3:
            print('=' * 10, 3)
            li = Items.objects.filter(
                theme=Themes.objects.get(name=catalogPath[2]).id)
            print('=' * 10, 3)

    print(li)
    context = {
        'title': 'Каталог',
        'req': catalogPath,
        'items': li,
    }
    if len(li) == 0:
        returnHtml = 'main/Home.html'
    return render(request,returnHtml,context=context)

def auth(request):
    return render(request,'main/auth.html',{'title':'Authorization'})

def personalAccount(request):
    return render(request,'main/personalAccount.html',{'title':'PA'})
