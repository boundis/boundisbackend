from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    (r'^locations/', include('locations.urls', namespace="locations")),
    url(r'^teams/', include('teams.urls')),
    url(r'^bugger/', include('bugger.urls')),
	url(r'^myprofile/$', 'user_profile.views.user_profile'),
	url(r'^myprofile/', include('user_profile.urls')),
    url(r'^accounts/', include('user_profile.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)

