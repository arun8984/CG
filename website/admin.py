from django.contrib import admin
from .models import Services,Currencies

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['ServiceName','Enabled']


admin.site.register(Currencies)
admin.site.register(Services,ServiceAdmin)