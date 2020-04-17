from django.contrib import admin
from .models import TypeDownTime, ObjectDownTime, Work, DownTime


# Register your models here.
@admin.register(TypeDownTime)
class TypeDownTimeAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'order',)
    list_editable = ('comment', 'order',)


@admin.register(ObjectDownTime)
class ObjectDownTimeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('date', 'obj', 'comment_one', 'comment_two',)
    list_editable = ('comment_one', 'comment_two',)


@admin.register(DownTime)
class DownTimeAdmin(admin.ModelAdmin):
    list_display = ('work', 'type', 'amount', 'smena')
    list_editable = ('type', 'amount', 'smena')
