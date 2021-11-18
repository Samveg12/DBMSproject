from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from country.models import finaltable,countries
from bootstrap_datepicker_plus import DateTimePickerInput 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.mail import send_mail
from .models import Emails


# Create your views here.


def mail(countrys,disaster,Lattitud,Longitud,severity,startdate,enddate,city,radius,additionalInfo):
	mailto = Emails.objects.filter(country = countries.objects.get(name = countrys))
	for user in mailto:
		send_mail(
		    subject = "alert",
		    message = f'{countrys},{disaster},{Lattitud},{Longitud},{severity},{startdate},{enddate},{city},{radius},{additionalInfo}',
		    from_email = "samvegvshah13@gmail.com",
		    recipient_list = [user.email],
		    fail_silently = False,
		)
		print(user.email)

class Create(LoginRequiredMixin,CreateView):
	model = finaltable
	template_name = "source/create.html"
	fields = ("__all__")
	success_url = "/source/all"
	def get_form(self):
		form = super(Create,self).get_form()
		form.fields['startdate'].widget = DateTimePickerInput()
		form.fields['enddate'].widget = DateTimePickerInput()
		return form 
	def form_valid(self, form):
		country = form.instance.country
		disaster = form.instance.disaster
		Lattitud = form.instance.Lattitud
		Longitud = form.instance.Longitud
		severity = form.instance.severity
		startdate = form.instance.startdate
		enddate = form.instance.enddate
		city = form.instance.city
		radius = form.instance.radius
		additionalInfo = form.instance.additionInfo
		mail(country,disaster,Lattitud,Longitud,severity,startdate,enddate,city,radius,additionalInfo)
		return super().form_valid(form)	
		
	

class All(LoginRequiredMixin,ListView):
	model = finaltable
	template_name="source/list.html"
	context_object_name="final"


class updates(LoginRequiredMixin,UpdateView):
	model = finaltable
	template_name = "source/update.html"
	fields = ("__all__")
	success_url = "/source/all"
	def get_form(self):
		form = super(updates,self).get_form()
		form.fields['startdate'].widget = DateTimePickerInput()
		form.fields['enddate'].widget = DateTimePickerInput()
		return form 

class deletes(LoginRequiredMixin,DeleteView):
	model = finaltable
	template_name = "source/delete.html"
	success_url = "/source/all"