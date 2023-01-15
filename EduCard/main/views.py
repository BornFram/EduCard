from django.http import HttpResponse
from django.shortcuts import render
from .models import *

from .logics import *



items =[('mema', 'moma'), ('aoaoa','weqwe'),('asddsdsa','dfs'),('dsf d','df dfs')]


def catalog(request):
    return render(request,'main/catalog.html',
                  {
                   'title':'Каталог',
                   'items': items,
                   })

def auth(request):
    return render(request,'main/auth.html',{'title':'Authorization'})

def personalAccount(request):
    return render(request,'main/personalAccount.html',{'title':'PA'})
