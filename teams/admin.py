from django.contrib import admin
from teams.models import UserProfile,Membership,Group

admin.site.register(Group)
admin.site.register(Membership)