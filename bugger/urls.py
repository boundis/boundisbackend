from django.conf.urls import patterns, include, url
from bugger import views

urlpatterns = patterns('',
        url(r'^create', 'bugger.views.create_bug'),
	url(r'^assigned/me','bugger.views.listBugsOwner'),
        url(r'^', 'bugger.views.listBugs'),        
)

