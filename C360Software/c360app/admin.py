from django.contrib import admin
from .models import Patient

# Register your models here.
# class BlogAdminArea(admin.AdminSite):
#     site_header = 'C360Soft'
admin.site.register(Patient)