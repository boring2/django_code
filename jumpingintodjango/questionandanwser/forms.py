from django import forms
from questionandanwser.models import Question

#class QuestionForm(forms.Form):
#	subject = forms.CharField(required=True,max_length=100)
#	description = forms.CharField(widget=forms.Textarea,required=True)

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		exclude = ('pub_date',)
