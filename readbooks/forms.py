from django import forms
from .import models

class CreateReview(forms.ModelForm):
  	class Meta:
  		model = models.Review
  		fields = ['title','rating','content']