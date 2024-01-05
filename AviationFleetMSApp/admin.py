from django.contrib import admin
from .models import Aircraft, Asset, MaintenanceHistory, CarbonEmissions, Communication


class AircraftAdmin(admin.ModelAdmin):
    list_display = ('aircraft_id_display', 'model', 'manufacturer', 'status')
    search_fields = ('aircraft_id', 'model', 'manufacturer')

    def aircraft_id_display(self, obj):
        return obj.aircraft_id

    aircraft_id_display.short_description = 'Aircraft ID'


class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_id_display', 'type', 'manufacturer', 'status')
    search_fields = ('asset_id', 'type', 'manufacturer')

    def asset_id_display(self, obj):
        return obj.asset_id

    asset_id_display.short_description = 'Asset ID'


class MaintenanceHistoryAdmin(admin.ModelAdmin):
    list_display = ('aircraft', 'asset', 'maintenance_type', 'maintenance_date')
    search_fields = ('aircraft__aircraft_id', 'asset__asset_id', 'maintenance_type')


class CarbonEmissionsAdmin(admin.ModelAdmin):
    list_display = ('aircraft', 'emission_date', 'emission_value', 'emission_source')
    search_fields = ('aircraft__aircraft_id', 'emission_source')


class CommunicationAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'timestamp', 'status')
    search_fields = ('sender', 'recipient')


# Register your models with the admin site
admin.site.register(Aircraft, AircraftAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(MaintenanceHistory, MaintenanceHistoryAdmin)
admin.site.register(CarbonEmissions, CarbonEmissionsAdmin)
admin.site.register(Communication, CommunicationAdmin)
