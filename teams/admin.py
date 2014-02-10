from django.contrib import admin
from teams.models import Person,Membership,Group

admin.site.register(Person)
admin.site.register(Group)
admin.site.register(Membership)