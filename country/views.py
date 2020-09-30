from django .http import HttpResponse
from .models import countries
from .models import finaltable
from .models import disaster


from django.shortcuts import render
def index(request):
    country=countries.objects.all()
    parameter={'count':country}
    return render(request,'country/index.html',parameter)
def country(request,id):
    all=[]
    y=countries.objects.filter(id=id)
    s=finaltable.objects.filter(country=id)
    set=[item.disaster for item in s]
    print(set)
    for j in set:
        disaste=disaster.objects.filter(name=j)
        all.append(disaste)
    
    parameter={'count':s,'all':all}
    print(parameter)
    return render(request,'country/country.html',parameter)
