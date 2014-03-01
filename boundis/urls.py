from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^locations/', include('locations.urls')),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^profile/', include('user_profiles.urls')),
    url(r'^teams/', include('teams.urls')),
    (r'^$', 'locations.views.home'),
    (r'^home/', 'user_profiles.views.my_profile'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}))