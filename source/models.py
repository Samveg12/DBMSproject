from django.db import models
from country.models import countries

# Create your models here.
class Emails(models.Model):
	name = models.CharField(max_length=120)
	email = models.EmailField()
	country = models.ForeignKey(countries,on_delete=models.CASCADE)