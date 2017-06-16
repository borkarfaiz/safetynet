from django.contrib import admin

from .models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'mobile_number', ]
    ordering = ['id']


class GiveToEmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'size_a', 'size_b', 'date', 'quantity', ]


class TakenFromEmployeeAdmin(admin.ModelAdmin):
    pass


class EmployeeAdvanceAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_id', 'amount', 'date']
    ordering = ['amount']


class ProviderAdmin(admin.ModelAdmin):
    pass


class GivenToProviderAdmin(admin.ModelAdmin):
    pass


class TakenFromProviderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(GivenToEmployee, GiveToEmployeeAdmin)
admin.site.register(TakenFromEmployee, TakenFromProviderAdmin)
admin.site.register(EmployeeAdvance, EmployeeAdvanceAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(GivenToProvider, GivenToProviderAdmin)
admin.site.register(TakeFromProvider, TakenFromProviderAdmin)
