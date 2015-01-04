from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.template import RequestContext 
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from questionandanwser.models import Question
from questionandanwser.forms import QuestionForm
# Create your views here.
def index(request):
	question_list = Question.objects.all()
	return render(request,'index.html',{'question_list':question_list})

def details(request,q_id):
	question = get_object_or_404(Question,pk=q_id)
	return render(request,'details.html', {'question':question})

@login_required
def createForm(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			subject = cd['subject']
			description = cd['description']
			#q = Question(subject=subject,description=description,pub_date=timezone.now())	
			#q.save()
			form.save()
			return HttpResponseRedirect(reverse('index'))
	else:
		form = QuestionForm()
	return render(request,'createq.html',{'form':form},context_instance=RequestContext(request))
@login_required
def editForm(request,q_id):
	question = get_object_or_404(Question,pk=q_id)
	if request.method == 'POST':
		form = QuestionForm(request.POST,instance=question)
		if form.is_valid():
			cd = form.cleaned_data
			subject = cd['subject']
			description = cd['description']
			#q = Question(subject=subject,description=description,pub_date=timezone.now())
			#q.save()
			form.save()
			return redirect('details',q_id)
	else:
		form = QuestionForm(instance=question)
	return render(request,'editq.html',{'form':form},context_instance=RequestContext(request))

