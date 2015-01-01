from django.conf.urls import patterns, include, url
from polls import views
urlpatterns = patterns('',
	#url(r'^$', views.index, name='index'),
	#url(r'(?P<poll_id>\d+)/$', views.details, name='details'),
	#url(r'(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'(?P<pk>\d+)/$', views.DetailsView.as_view(), name='details'),
	url(r'(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
	url(r'(?P<pk>\d)/results/$', views.ResultsView.as_view(), name='results'),
)
