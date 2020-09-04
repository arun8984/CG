from django.contrib import admin
from eav.admin import BaseEntityInline,BaseEntityAdmin
from eav.forms import BaseDynamicEntityForm
from .models import Profiles,Partners,PartnerTypes,ProfileImages

class PartnerAdmin(admin.ModelAdmin):
    list_display = ['Partner','AccountType','Email','Phone','Verified','Enabled']

    def Partner(self, obj):
        return obj.FirstName + ' ' + obj.LastName if obj.AccountType == PartnerTypes.INDIVIDUAL else obj.BusinessName

class ProfileAdminForm(BaseDynamicEntityForm):
    model = Profiles

class ProfileImagesInline(admin.TabularInline):
    model = ProfileImages
    fields = ['Image','image_tag']
    readonly_fields = ['image_tag']

#class ProfilesAdmin(BaseEntityInline, admin.StackedInline):
class ProfilesAdmin(BaseEntityAdmin):
    form = ProfileAdminForm
    inlines = [ProfileImagesInline]


admin.site.register(Partners, PartnerAdmin)
admin.site.register(Profiles, ProfilesAdmin)
