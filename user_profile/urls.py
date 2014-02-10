from django.conf.urls import patterns, url
urlpatterns = patterns('',
 url(r'^profile/$', 'user_profile.views.user_profile'),
	(r'^add$', 'user_profile.views.add_user'),
)

    