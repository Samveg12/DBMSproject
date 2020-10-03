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

class Helpline(models.Model):
    country=models.ForeignKey(countries,on_delete=models.CASCADE,null=True)
    disaster=models.ForeignKey(disaster,on_delete=models.CASCADE,null=True)
    Number = models.CharField(max_length=12)
    def __str__(self):
        return self.country.__str__()
class finaltable(models.Model):
    country=models.ForeignKey(countries,on_delete=models.CASCADE,null=True)
    disaster=models.ForeignKey(disaster,on_delete=models.CASCADE,null=True)
    Lattitud=models.DecimalField(max_digits=19, decimal_places=4, blank = True, default =22.35, null = True)
    Longitud=models.DecimalField(max_digits=19, decimal_places=4, blank = True, default =33.55, null = True)
    severity=models.CharField(max_length=100,null=True)
    startdate=models.DateTimeField(auto_now_add=False , editable=True,null=True)
    enddate=models.DateTimeField(auto_now_add=False , editable=True,null=True)
    city = models.CharField(max_length = 100,default="Mumbai")
    radius=models.IntegerField(default=0)
    additionInfo = models.TextField()
    def __str__(self):
        return self.country.__str__()

class History(models.Model):
    country=models.ForeignKey(countries,on_delete=models.CASCADE,null=True)
    disaster=models.ForeignKey(disaster,on_delete=models.CASCADE,null=True)
    Lattitud=models.DecimalField(max_digits=19, decimal_places=4, blank = True, default =22.35, null = True)
    Longitud=models.DecimalField(max_digits=19, decimal_places=4, blank = True, default =33.55, null = True)
    severity=models.CharField(max_length=100,null=True)
    startdate=models.DateTimeField(auto_now_add=False , editable=True,null=True)
    enddate=models.DateTimeField(auto_now_add=False , editable=True,null=True)
    city = models.CharField(max_length = 100,default="Mumbai")
    radius=models.IntegerField(default=0)
    additionInfo = models.TextField()
    def __str__(self):
        return self.country.__str__()