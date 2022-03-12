from django.db import models
from django.db.models import Q


# таблица цистерны
class MilkTank(models.Model):
    fullness = models.IntegerField("Числовой показатель заполненности")

    def fulling(self, liters):
        self.fullness += int(liters)

    # подкласс для корректного вывода названий в админке
    class Meta:
        verbose_name = 'Цистерна'
        verbose_name_plural = 'Цистерны'


# таблица сеансов заполнения цистерны
class Fulling(models.Model):

    milk_tank = models.ForeignKey(MilkTank, on_delete=models.CASCADE)
    name = models.CharField("Имя заливающего", max_length=30)
    liters = models.IntegerField("Число залитых литров")
    comment = models.CharField("Комментарий к заливке", max_length=50)

    # подкласс для корректного вывода названий в админке
    class Meta:
        verbose_name = 'Заливка'
        verbose_name = 'Заливки'
