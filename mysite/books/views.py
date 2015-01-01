from django.shortcuts import render_to_response
from books.models import Book
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def search(request):
	errors = []
	if 'p' in request.GET:
		bookname = request.GET['p']
		if not bookname:
			errors.append('Enter a search term.')
		elif len(bookname) > 20:
			errors.append('Please enter at most 20 characters.')
		else:
			books = Book.objects.filter(title__icontains=bookname)
			return render_to_response("search_result.html",{'books':books,'query':bookname})
	return render_to_response('search_form.html',{'errors':errors})


