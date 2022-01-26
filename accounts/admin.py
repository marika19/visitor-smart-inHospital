from django.contrib import admin
# CustomUserをインポート
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'email',
        'last_name', 'first_name',
        'birthday', 'postal_code', 'address', 'tel', 'patient_id', 'patient_name', 'relationship1',
        'is_staff', 'is_active',
    )
    list_display_links = ('email', 'patient_id')
    list_filter = (
        'email', 'patient_id',
        'last_name', 'first_name',
        'is_staff', 'is_active',
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',  'last_name', 'first_name',
                     'patient_name', 'patient_id',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
