from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from forms import ContactForm
'''
def contact(request):
	errors = []
	if request.method == 'POST':
		if not request.POST.get('subject',''):
			errors.append('Enter a subject')
		if not request.POST.get('message',''):
			errors.append('Enter a message')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Enter a valid e-mail address.')
		if not errors:
		#	send_mail('subject', 'this is the message of email', 'code_zhen@163.com', ['510694395@qq.com'], fail_silently=True)
			send_mail(request.POST['subject'],request.POST['message'],'code_zhen@163.com',[request.POST.get('email','code_zhen@163.com')],fail_silently=False)
			return HttpResponseRedirect('/contact/thanks/')
	return render_to_response('contact_form.html',{'errors':errors},context_instance=RequestContext(request))
'''

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			print 'cd-------------->'+str(cd.get('email','ssssss'))
			send_mail(cd['subject'],cd['message'],'code_zhen@163.com',['510694395@qq.com'],auth_user='code_zhen@163.com',auth_password='xxxxxxxxxxxxxxxxxxxx',fail_silently=True)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(initial={'subject':'i love your site!'})
	return render_to_response('contact_form.html',{'form':form},context_instance=RequestContext(request))
def thanks(request):
	return HttpResponse('thanks')				
