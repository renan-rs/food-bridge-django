from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        'username',
        'email',
        'role',
        'is_verified',
        'is_staff',
    ]

    list_filter = ['role', 'is_verified', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (
            'Informações Adicionais (Marketplace)',
            {
                'fields': (
                    'role',
                    'phone',
                    'address',
                    'latitude',
                    'longitude',
                    'is_verified',
                )
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'Informações Adicionais (Marketplace)',
            {
                'fields': (
                    'role',
                    'phone',
                    'address',
                    'is_verified',
                )
            },
        ),
    )