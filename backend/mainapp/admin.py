from django.contrib import admin

from .models import DroneCategory,Drones,Orders,Features

admin.site.register(DroneCategory)
admin.site.register(Drones)
admin.site.register(Orders)
admin.site.register(Features)
