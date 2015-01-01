from django.shortcuts import render,get_object_or_404
from polls.models import Poll,Choice
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
#from django.http import Http404
# Create your views here.
#def index(request):
#	lastest_polls_list = Poll.objects.order_by('-pub_date')[:5]
#	return render(request,'polls/index.html',{'lastest_polls_list':lastest_polls_list})

#def details(request,poll_id):
	#try:
	#	poll = Poll.objects.get(pk=poll_id)
	#except Poll.DoesNotExist:
	#	raise Http404()
#	poll = get_object_or_404(Poll,pk=poll_id)
#	return render(request,'polls/details.html',{'poll':poll})

#def results(request, poll_id):
#	poll = get_object_or_404(Poll,pk=poll_id)
#	return render(request,'polls/results.html',{'poll':poll})	
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'lastest_polls_list'
	def get_queryset(self):
		return Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailsView(generic.DetailView):
	template_name = 'polls/details.html'
	model = Poll
	def get_queryset(self):
		return Poll.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	template_name = 'polls/results.html'
	model = Poll
def vote(request, poll_id):
	poll = get_object_or_404(Poll,pk=poll_id)
	try:
		select_choice = poll.choice_set.get(pk=request.POST['selectvote'])
	except KeyError,Choice.DoesNotExist:
		return render(request,'polls/details.html',{'poll':poll,'error_message':'no the choice id'})
	else:
		select_choice.votes += 1
		select_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(poll.id,)))

