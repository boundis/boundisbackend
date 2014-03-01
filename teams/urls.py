from django.conf.urls import patterns, url
urlpatterns = patterns('',
 url(r'^$', 'teams.views.listMembership'),
 url(r'^group/create/', 'teams.views.create_group'),
 url(r'^group/(\d+)/$', 'teams.views.group_detail'),
)
