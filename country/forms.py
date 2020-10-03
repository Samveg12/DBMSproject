from django import forms
from source.models import Emails

    

class Email(forms.ModelForm):
    class Meta:
        model=Emails
        fields = "__all__"
        
