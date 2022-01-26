from django.contrib import admin
from .models import Reception0, Reception1,  Reception2, Reception3


# Register your models here.

class Reception0Admin(admin.ModelAdmin):
    model = Reception0
    list_display = ('email', 'purpose',
                    'accompany', 'companion_last_name', 'companion_first_name', 'relationship2')
    list_filter = ('purpose', 'accompany', 'relationship2')
    search_fields = ('email','companion_last_name', 'companion_first_name',)


class Reception1Admin(admin.ModelAdmin):
    model = Reception1
    list_display = ('email', 'bt1', 'bt2', 'InHospital')
    search_fields = ('email','bt1', 'bt2')



class Reception2Admin(admin.ModelAdmin):
    model = Reception2
    list_display = ('email', 'purpose',
                    'accompany',
                    'companion_last_name',
                    'companion_first_name', 'relationship2', 'bt1', 'bt2', 'InHospital')
    list_filter = ('purpose', 'accompany', 'InHospital','relationship2',)
    search_fields = ( 'companion_last_name',
                    'companion_first_name', 'bt1', 'bt2', )


class Reception3Admin(admin.ModelAdmin):
    model = Reception3
    list_display = ('email', 'OutHospital')
    search_fields = ('email','OutHospital')


admin.site.register(Reception0, Reception0Admin)
admin.site.register(Reception1, Reception1Admin)
admin.site.register(Reception2, Reception2Admin)
admin.site.register(Reception3, Reception3Admin)
