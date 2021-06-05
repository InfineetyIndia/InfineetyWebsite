from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.

from .models import PlanType, Plan

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "price")

@admin.register(PlanType)
class PlanTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "display_name")

# admin.site.register(PlanType)
admin.site.unregister(Group)
