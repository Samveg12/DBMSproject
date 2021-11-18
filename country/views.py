from django .http import HttpResponse
from .models import countries
from .models import finaltable,History,Helpline
from .models import disaster
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import Email
from django.core.mail import send_mail
import datetime
from django.utils import timezone





from django.shortcuts import render,redirect

def mail(name,email,country):
    send_mail(
        subject = "alert",
        message = f'thanks {name} for registering for {country}',
        from_email = "samvegvshah13@gmail.com",
        recipient_list = [email],
        fail_silently = False,
    )

class index(ListView):
    model = countries
    template_name="country/index.html"
    context_object_name="count"

def country(request,id):
    now = timezone.now()
    print(now)
    all=[]
    y=countries.objects.filter(id=id)
    s=finaltable.objects.filter(country=id)
    for i in s:
        if i.enddate != None:
            if now>i.enddate:
                history = History(country=i.country,disaster=i.disaster,Lattitud=i.Lattitud,Longitud=i.Longitud,severity=i.severity,startdate=i.startdate,enddate=i.enddate,city=i.city,radius=i.radius,additionInfo=i.additionInfo)
                history.save()
                i.delete()
    set=[item.disaster for item in s]
    hist = History.objects.filter(country = id)
    parameter={'count':s,'hist':hist}
    return render(request,'country/country.html',parameter)
class Disaster(DetailView):
    model = finaltable
    template_name="country/disaster.html"
    def get_context_data(self, **kwargs):
            context = super(Disaster, self).get_context_data(**kwargs)
            country = finaltable.objects.get(pk = self.kwargs.get('pk')).country
            disaster = finaltable.objects.get(pk = self.kwargs.get('pk')).disaster
            helpline = Helpline.objects.filter(country = country).get(disaster = disaster).Number
            print(helpline)

            context['helpline'] =helpline
            print(context['helpline'])
            return context
    context_object_name = "count"

class HistoryApp(DetailView):
    model = History
    template_name="country/disaster.html"
    def get_context_data(self, **kwargs):
            context = super(HistoryApp, self).get_context_data(**kwargs)
            country = History.objects.get(pk = self.kwargs.get('pk')).country
            disaster = History.objects.get(pk = self.kwargs.get('pk')).disaster
            helpline = Helpline.objects.filter(country = country).get(disaster = disaster).Number
            print(helpline)

            context['helpline'] =helpline
            print(context['helpline'])
            return context
    context_object_name = "count"


def thankyou(request):
    return render(request,'country/thankyou.html')

def register(request):
    if request.method ==  "POST":
        form = Email(request.POST)
        if form.is_valid():
            print("HITUZhfb")
            Name = form.cleaned_data['name']
            print(Name)
            email = form.cleaned_data['email']
            print(email)
            Country = form.cleaned_data['country']
            print(Country)
            mail(Name,email,Country)
            form.save()
            return redirect('/')
        return redirect('/register')
    form = Email()
    return render(request,"country/register.html",{"form":form})


