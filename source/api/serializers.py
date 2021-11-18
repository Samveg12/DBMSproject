from django.db.models import fields
from rest_framework import serializers
from source.models import Emails
from country.models import countries,disaster,Helpline,finaltable,History

class counriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=countries
        fields=['name','image']
    
class finalSerializer(serializers.ModelSerializer):
    class Meta:
        model=finaltable
        fields=['country','disaster','Lattitud','Longitud','severity','startdate','enddate','city','radius']
