from django.contrib import admin
from .models import Record




class RegisterAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'first_name', 'last_name', 'email', 'phone', 'city', 'state']


admin.site.register(Record, RegisterAdmin)