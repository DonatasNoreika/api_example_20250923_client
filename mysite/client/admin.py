from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('api_token',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
