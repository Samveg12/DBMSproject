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
    parameter={'count':s,'all':all}
    return render(request,'country/country.html',parameter)
def disaster(request,id):
    all=[]
    s=finaltable.objects.filter(id=id)
    set=[item.disaster for item in s]
    print(s)
    parameter={'count':s,'all':all}
    return render(request,'country/disaster.html',parameter)
