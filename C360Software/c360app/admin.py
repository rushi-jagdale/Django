from django.contrib import admin
from .models import Patient

# Register your models here.
# 
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','gender','address')
   
    list_per_page = 4

admin.site.register(Patient,PatientAdmin)