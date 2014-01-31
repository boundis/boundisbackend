from django.contrib import admin
from .models import Sport,Category,Facility_type,Surface_type
# Register your models here.

class sportAdmin(admin.ModelAdmin):
	list_display = ('name', 'category')
	list_filter = ['category']
	search_fields = ['name']

admin.site.register(Sport, sportAdmin)
admin.site.register(Category)
admin.site.register(Facility_type)
admin.site.register(Surface_type)
