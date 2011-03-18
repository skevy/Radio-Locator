from django.contrib.gis import admin
from models import Station

class StationAdmin(admin.OSMGeoAdmin):
    list_display = ['call_letters', 'frequency', 'city', 'state', 'format']
    list_filter = ['format']
    search_fields = ['call_letters', 'frequency']

admin.site.register(Station, StationAdmin)