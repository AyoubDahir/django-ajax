from django.contrib import admin
from . models import  patient
# Register your models here.

class paientAdmin(admin.ModelAdmin):
    list_display = ('fullname','age','address','phone','date_created')

admin.site.register(patient, paientAdmin)

