from django.db import models


class countries(models.Model):
    name=models.CharField(max_length=100,default="enter")
    image=models.ImageField(upload_to='country/images')
    def __str__(self):
        return self.name
class disaster(models.Model):
    name=models.CharField(max_length=100,default="enter")
    image=models.ImageField(upload_to='country/images')
    precautions = models.TextField(max_length=250, blank=True)
    def __str__(self):
	    return self.name
class safehaven(models.Model):
    name=models.CharField(max_length=100,default="enter")
    def __str__(self):
    	return self.name
class transport(models.Model):
    name=models.CharField(max_length=100,default="enter")
    def __str__(self):
    	return self.name
class finaltable(models.Model):
    country=models.ForeignKey(countries,on_delete=models.CASCADE,null=True)
    disaster=models.ForeignKey(disaster,on_delete=models.CASCADE,null=True)
    Lattitude=models.CharField(max_length=100,default="lattitude",null=True)
    Longitude=models.CharField(max_length=100,default="longitude",null=True)
    severity=models.CharField(max_length=100,null=True)
    startdate=models.DateField(null=True)
    enddate=models.DateField(null=True)
    #startTime=models.TimeField(auto_now_add=True,null=True)
    #endTime=models.TimeField(auto_now_add=True,null=True)
    transport=models.ManyToManyField(transport)
    safehaven=models.ManyToManyField(safehaven)
    def __str__(self):
    	return self.country.__str__()