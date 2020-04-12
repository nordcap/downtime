from django.db import models
from django.utils import timezone

# Типы простоев
from django.utils.datetime_safe import datetime


class TypeDownTime(models.Model):
    name = models.CharField(max_length=3, verbose_name="Название простоя", unique=True)
    comment = models.CharField(max_length=100, verbose_name="Пояснение (расшифровка)", default='')
    order = models.PositiveSmallIntegerField(verbose_name="Порядковый номер", default=0, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип простоя"
        verbose_name_plural = "Типы простоя"
        ordering = ['order']


# Объекты учета простоев
class ObjectDownTime(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название оборудования", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объект простоя"
        verbose_name_plural = "Объекты простоя"
        ordering = ['name']


# Комментарии к производимым каждый день работам
class WorkDownTime(models.Model):
    date = models.DateField(verbose_name="Дата работ", db_index=True, default=timezone.now)
    obj = models.ForeignKey(ObjectDownTime, on_delete=models.PROTECT, verbose_name="Объект")
    comment_one = models.CharField(max_length=1000, verbose_name="Комментарий к работам в 1 смену", default='', blank=True)
    comment_two = models.CharField(max_length=1000, verbose_name="Комментарий к работам в 2 смену", default='', blank=True)

    def __str__(self):
        return "{0}: {1}".format(self.date, self.obj)

    class Meta:
        verbose_name = "Производимые работы"
        verbose_name_plural = "Производимые работы"
        ordering = ['-date']


# Рабочая таблица - время простоев оборудования
class DownTime(models.Model):
    SMENA = (
        ('1', '1 смена'),
        ('2', '2 смена')
    )
    date = models.DateField(verbose_name="Дата", db_index=True, default=timezone.now)
    smena = models.CharField(max_length=1, choices=SMENA, verbose_name="Смена", default='1')
    type_downtime = models.ForeignKey(TypeDownTime, on_delete=models.PROTECT, verbose_name="Тип простоя")
    amount = models.TimeField(verbose_name="Время простоя")

    def __str__(self):
        return "{0} - {1}".format(self.date, self.type_downtime)

    class Meta:
        verbose_name = "Простои"
        verbose_name_plural = "Простои"
        ordering = ['-date']
