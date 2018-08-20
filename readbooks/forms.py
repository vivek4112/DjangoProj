from django import forms
from .import models

class CreateReview(forms.ModelForm):
  	class Meta:
  		model = models.Review
  		fields = ['title','rating','content']
  		widgets = {'title': forms.TextInput(attrs={'class': 'form-control'}),
  		           'rating': forms.NumberInput(attrs={'class': 'form-control','min':1,'max':5}),
                   'content': forms.Textarea(attrs={'class': 'form-control'}),
                   }