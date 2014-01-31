from django.contrib import admin
from .models import Continent,Country,State,Suburb,Venue,Facility,Venuepic,Facilitypic


class CountryAdmin(admin.ModelAdmin):
	list_display = ('country', 'continent')
	list_filter = ['continent']
	search_fields = ['country']
	ordering = ['country']

class StateAdmin(admin.ModelAdmin):
	list_display = ('state', 'abbreviation', 'country')
	list_filter = ['country']
	search_fields = ['state']
	ordering = ['state']

class SuburbAdmin(admin.ModelAdmin):
	list_display = ('suburb', 'state', 'country')
	list_filter = ['state']
	search_fields = ['suburb']
	ordering = ['suburb']

class VenueAdmin(admin.ModelAdmin):
	list_display = ('name', 'street_address','suburb', 'state', 'country')
	list_filter = ['suburb']
	search_fields = ['name']
	fieldsets = (
		('Name', {'fields':('name',)}),
        ('Address', {'fields': ('street_address', 'suburb')}),
        ('Contact information', {'fields':('phone_number', 'email', 'website')}),
        ('Features', {'fields': ('public_toilets', 'change_rooms', 'onsite_parking')}),
        ('Opening hours', {'fields':(('monday_is_closed', 'monday_op','monday_cl'),('tuesday_is_closed', 'tuesday_op','tuesday_cl'),('wednesday_is_closed', 'wednesday_op','wednesday_cl'),('thursday_is_closed', 'thursday_op','thursday_cl'),('friday_is_closed', 'friday_op','friday_cl'),('saturday_is_closed', 'saturday_op','saturday_cl'),('sunday_is_closed', 'sunday_op','sunday_cl'))})
    )

class FacilityAdmin(admin.ModelAdmin):
	list_display = ('sports', 'venue')
	list_filter = ['sports']
	search_fields = ['sports']

admin.site.register(Continent)
admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Suburb, SuburbAdmin)
admin.site.register(Venue, VenueAdmin) 
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Venuepic)
admin.site.register(Facilitypic)



