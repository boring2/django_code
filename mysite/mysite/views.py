from django.http import HttpResponse
import datetime
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response

def current_datetime(request):
	now = datetime.datetime.now()
	#t = get_template("current_datetime.html")
	#html = t.render(Context({"current_date":now}))
	#return HttpResponse(html)
	mydict = {"current_date":now}
	return render_to_response("current_datetime.html",mydict)

def hours_ahead(request, offset):
	offset = int(offset)
	#assert False,"ssss"
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	#html = "<html><body>In %s hour(s),it will be %s.</body></html>" % (offset, dt)
	#return HttpResponse(html)
	return render_to_response("hours_ahead.html",{"hour_offset":offset,"next_time":dt})

def display_meta(request):
	values = request.META
	path = request.path
	#values.sort()
	return render_to_response("display_meta.html",{"values":values,'path':'path'})



