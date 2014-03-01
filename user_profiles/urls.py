from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^myprofile', 'user_profiles.views.my_profile'),
    url(r'^(\d+)', 'user_profiles.views.user_profile'),
    url(r'^editprofile', 'user_profiles.views.edit_UserProfile'),
)
