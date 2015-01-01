from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import current_datetime,hours_ahead,display_meta
from books import views
from contact.views import contact,thanks 
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$',current_datetime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^display_meta/$',display_meta),
	url(r'^search/$',views.search),
	url(r'^contact/$',contact),
	url(r'^contact/thanks/$',thanks),
)
