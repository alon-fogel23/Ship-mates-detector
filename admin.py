from django.contrib import admin
from .models import Department, Soldier, SingleRecord, Compartment

admin.site.register(Department)
admin.site.register(Soldier)
admin.site.register(SingleRecord)
admin.site.register(Compartment)
