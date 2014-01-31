from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    (r'^locations/', include('locations.urls', namespace="locations")),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
 {'document_root': settings.MEDIA_ROOT}),
    #(r'^$', include('locations.urls', namespace="locations")),
	 #url(r'^finder/location/(\d+)/$', 'finder.views.location_detail'),
     #url(r'^finder/add_location/$', 'finder.views.add_location'),
	 #url(r'^finder/add_location/approvals/$', 'finder.views.approvals'),
	 #url(r'^finder/add_location/approvals/approve/(\d+)/$', 'finder.views.approve'),
)
