from django.http import HttpResponse
from django.shortcuts import render
import json
import os.path
from .models import *
from .logics import *
from .config import *

config = json.load(open('.config/serviceConfig.json'))


def catalog(request,catalogPath):
    catalogPath = catalogPath.split('/')
    li = [0]
    li.append(1)
    match len(catalogPath):
        case 1:
            li = Classes.objects.get(name=catalogPath[0])
        case 2:
            li = Classes.objects.get(name=catalogPath[0])

    li = Items.objects.filter(
        theme=Themes.objects.get(
            name=catalogPath[2],
            subject=Subjects.objects.get(
                name=catalogPath[1],
                clas=Classes.objects.get(
                    name=catalogPath[0]
                ).id
            ).id
        ).id
    )
    print(li)
    context = {
        'title': 'Каталог',
        'req': "5 класс/русский язык/стили речи/", #tested field
        'items': li,
    }
    return render(request,'main/catalog.html',context=context)


def home(request, clas):
    context = {
        'title': 'EduCard',
        'classList': clas,
        'popularItemList': Items.objects.filter(raiting__gte=config.get('mpr')),
    }
    return render(request, 'main/home.html', context=context)


def auth(request):
    return render(request,'main/auth.html',{'title':'Authorization'})

def personalAccount(request):
    return render(request,'main/personalAccount.html',{'title':'PA'})
