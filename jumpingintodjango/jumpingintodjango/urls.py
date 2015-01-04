from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jumpingintodjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^login/$','jumpingintodjango.views.login_page',name='login_page'),
	url(r'^logout/$','jumpingintodjango.views.logout_page',name='logout_page'),
	url(r'^$','jumpingintodjango.views.homepage',name='homepage'),
	url(r'^question/$','questionandanwser.views.index',name='index'),
	url(r'^question/details/(?P<q_id>\d+)/$','questionandanwser.views.details',name='details'),
	url(r'^question/createq/$','questionandanwser.views.createForm',name="createForm"),
	url(r'^question/edit/(?P<q_id>\d+)/$','questionandanwser.views.editForm',name='edit'),
    url(r'^admin/', include(admin.site.urls)),
)
