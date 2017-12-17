from django import forms
from .models import Sets

class SetsForm(forms.ModelForm):
	pass
#	class Meta:
#		model = Sets
#		fields = ('title','text')

class UploadPhotoToSets(forms.ModelForm):
	class Meta:
		model = Sets	
		fields = ('title', 'text')
