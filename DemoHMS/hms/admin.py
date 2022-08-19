from django.contrib import admin
from hms.models import Appointment
# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['name','email','mobileno']

