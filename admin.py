from django.contrib import admin
from .models import Department, Soldier, SingleRecord, Compartment,ViewMode


admin.site.register(Department)
admin.site.register(Soldier)
admin.site.register(SingleRecord)
admin.site.register(Compartment)
admin.site.register(ViewMode)

