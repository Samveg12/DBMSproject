from django.db import models
from country.models import countries


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.
class Emails(models.Model):
	name = models.CharField(max_length=120)
	email = models.EmailField()
	country = models.ForeignKey(countries,on_delete=models.CASCADE)
	image=models.ImageField(default=None,null=True,blank=True,upload_to='media/country')

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
	if(created):
		Token.objects.create(user=instance)