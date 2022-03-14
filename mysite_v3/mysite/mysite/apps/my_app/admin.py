from django.contrib import admin
from .models import MilkTank, Fulling, Worker


class FullingAdmin(admin.ModelAdmin):
    list_display = ('name', 'milk_tank', 'liters', 'comment')


class MilkTankAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullness')


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date')


admin.site.register(MilkTank, MilkTankAdmin)
admin.site.register(Fulling, FullingAdmin)
admin.site.register(Worker, WorkerAdmin)
