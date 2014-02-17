from django.conf.urls import patterns, url
urlpatterns = patterns('',
 	url(r'^teams/$', 'teams.views.listMembership'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/locations/search'}),
    url(r'^group/(\d+)', 'teams.views.group_detail'),
    url(r'^group/create/$', 'teams.views.create_group'),

)
