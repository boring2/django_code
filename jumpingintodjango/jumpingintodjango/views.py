from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout
from jumpingintodjango.forms import LoginForm

def login_page(request):
	message = None
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username,password=password)
			if user is not None:
				if  user.is_active:
					login(request,user)
					return redirect('index')
				else:
					message = "the user is not active"
			else:
				message = "invalid username/password."
	else:
		form = LoginForm()
	return render_to_response('login.html',{"form":form,"message":message},context_instance=RequestContext(request))

def homepage(request):
	return render_to_response('homepage.html',context_instance=RequestContext(request))

def logout_page(request):
	logout(request)
	return redirect('homepage')
