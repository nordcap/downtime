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
class Work(models.Model):
    date = models.DateField(verbose_name="Дата работ", db_index=True, default=timezone.now)
    obj = models.ForeignKey(ObjectDownTime, on_delete=models.PROTECT, verbose_name="Объект")
    type = models.ManyToManyField(TypeDownTime, through="DownTime", through_fields=('work', 'type'), null=True)
    comment_one = models.CharField(max_length=255, verbose_name="Комментарий к работам в 1 смену", default='', blank=True)
    comment_two = models.CharField(max_length=255, verbose_name="Комментарий к работам в 2 смену", default='', blank=True)

    def __str__(self):
        return "{0} на  {1}".format(self.date, self.obj)

    class Meta:
        verbose_name = "Производимые работы"
        verbose_name_plural = "Производимые работы"
        ordering = ['-date']


# Рабочая таблица - время простоев оборудования
class DownTime(models.Model):
    smena = (
        ('1', '1 смена'),
        ('2', '2 смена')
    )
    work = models.ForeignKey(Work, on_delete=models.CASCADE, verbose_name="Работы", related_name='works')
    type = models.ForeignKey(TypeDownTime, on_delete=models.CASCADE, verbose_name="Тип простоя", related_name='types')
    amount = models.TimeField(verbose_name="Время простоя")
    smena = models.CharField(max_length=1, choices=smena, verbose_name="Смена", default='1')

    def __str__(self):
        return "{0} {1} {2}".format(self.work, self.type, self.smena)

    class Meta:
        verbose_name = "Простои"
        verbose_name_plural = "Простои"
        ordering = ['-work']
