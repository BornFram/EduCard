from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .logics import *


def catalog(request,catalogPath):
    catalogPath = catalogPath.split('/')
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
        'req': catalogPath,
        'items': li,
    }
    return render(request,'main/catalog.html',context=context)

def auth(request):
    return render(request,'main/auth.html',{'title':'Authorization'})

def personalAccount(request):
    return render(request,'main/personalAccount.html',{'title':'PA'})
