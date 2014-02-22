from django.conf.urls import patterns, include, url
from bugger import views

urlpatterns = patterns('',
        url(r'^', 'bugger.views.listBugs'),        
	url(r'^create', 'bugger.views.create_bug'),
)

