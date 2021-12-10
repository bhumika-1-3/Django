from django import forms
from .models import input


# class data(forms.Form):
#     task=forms.CharField()
#     description=forms.CharField()


class data(forms.ModelForm):
    class Meta:
        model =input
        fields=[
            'task',
            'description',
            'compulsory',

        ]    
   
