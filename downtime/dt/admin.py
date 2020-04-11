from django.contrib import admin
from .models import TypeDownTime, ObjectDownTime, WorkDownTime, DownTime


# Register your models here.
@admin.register(TypeDownTime)
class TypeDownTimeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order',)


@admin.register(ObjectDownTime)
class ObjectDownTimeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(WorkDownTime)
class WorkDownTimeAdmin(admin.ModelAdmin):
    list_display = ('date', 'comment_one', 'comment_two',)


@admin.register(DownTime)
class DownTimeAdmin(admin.ModelAdmin):
    list_display = ('date', 'type_downtime', 'amount',)
