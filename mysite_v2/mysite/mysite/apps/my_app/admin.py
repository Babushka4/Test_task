from django.contrib import admin
from .models import MilkTank, Fulling


class FullingAdmin(admin.ModelAdmin):
    list_display = ('name', 'milk_tank', 'liters', 'comment')


class MilkTankAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullness')


admin.site.register(MilkTank, MilkTankAdmin)
admin.site.register(Fulling, FullingAdmin)
