from django.contrib import admin
from .models import Profile
# from .models import Location


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_num', 'address']


# class LocationAdmin(admin.ModelAdmin):
#     list_display = ['user', 'phone_num', 'x', 'y']


admin.site.register(Profile, ProfileAdmin)
# admin.site.register(Location, LocationAdmin)
