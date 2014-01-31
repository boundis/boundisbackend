from django.conf.urls import patterns, include, url
from locations import views



urlpatterns = patterns('',
	url(r'^$', 'locations.views.search'),
	url(r'^all_venues', 'locations.views.allvenues'),
	url(r'^(\d+)', 'locations.views.venue_detail', name = 'venue_detail'),
	url(r'^add_venue', 'locations.views.add_venue'),
	url(r'^add_facility/(\d+)', 'locations.views.add_facility'),
	url(r'^edit_facility/(\d+)', 'locations.views.edit_facility'),
	url(r'^edit_venue/(\d+)', 'locations.views.edit_venue'),
	url(r'^search/$', 'locations.views.search'),
	url(r'^search_locations/$', 'locations.views.search_locations'),
	url(r'^add_v_photos/(\d+)', 'locations.views.add_venuepic'),
	url(r'^add_f_photos/(\d+)', 'locations.views.add_facilitypic'),
    # Examples:
    # url(r'^$', 'boundis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

)