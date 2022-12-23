from django.contrib import admin
from .models import RMP,Patient,Doctor,Prescription,Slots,medicines,Appointments,Vitals

admin.site.register(RMP)
admin.site.register(Patient)
admin.site.register(Prescription)
admin.site.register(Slots)
admin.site.register(medicines)
admin.site.register(Appointments)
admin.site.register(Vitals)
admin.site.register(Doctor)

# Register your models here.
