from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class ModelAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields',{'fields':('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Fields', {'fields': ('date_of_birth',)})
    )