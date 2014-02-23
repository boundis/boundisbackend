from django.conf.urls import patterns, include, url
from bugger import views

urlpatterns = patterns('',
        url(r'^create', 'bugger.views.create_bug'),
        url(r'^bug/(\d+)', 'bugger.views.bugDetail'),
	url(r'^bug/edit/(\d+)', 'bugger.views.editBug'),
	url(r'^assigned/me','bugger.views.listBugsOwner'),
        url(r'^', 'bugger.views.listBugs'),        
)

