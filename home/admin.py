from django.contrib import admin
from home.models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ['qayerdan', 'qayerga', 'client_phone', 'client_name', 'person_count', 'price', 'status']
    readonly_fields = ['status', 'qayerdan', 'qayerga', 'client_phone', 'client_name', 'person_count', 'price', 'customer', 'driver']


class TempAdmin(admin.ModelAdmin):
    list_display = ['qayerdan', 'qayerga', 'client_phone', 'client_name', 'person_count', 'price', 'status']
    readonly_fields = ['status', 'qayerdan', 'qayerga', 'client_phone', 'client_name', 'person_count', 'price', 'customer']


class ArchOrderAdmin(admin.ModelAdmin):
    list_display = ['qayerdan', 'qayerga', 'client_phone', 'client_name', 'person_count', 'price', 'status']
    readonly_fields = ['status', 'qayerdan', 'qayerga', 'client_phone', 'client_name', 'person_count', 'price', 'customer', 'driver']


admin.site.register(TempOrder, TempAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ArchiveOrder, ArchOrderAdmin)
admin.site.register(User)
