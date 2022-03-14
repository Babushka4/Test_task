from django.db import models
from django.db.models import Q


# таблица цистерны
class MilkTank(models.Model):

    fullness = models.IntegerField("Числовой показатель заполненности")

    def __str__(self):
        return 'Цистерна ' + str(self.id)

    # заполнение цистерны
    def fulling(self, liters):
        self.fullness += int(liters)

    # определение статуса цистерны
    def get_status(self):
        if self.fullness == 300:
            return "Переполнена"
        elif self.fullness >= 250:
            return "Близка к заполнению"
        else:
            return "all right"

    # подкласс для корректного вывода названий в админке
    class Meta:
        verbose_name = 'Цистерна'
        verbose_name_plural = 'Цистерны'


# таблица сеансов заполнения цистерны
class Fulling(models.Model):

    def __str__(self):
        # не знаю что будет лучше возвращать, пока так
        return self.name

    milk_tank = models.ForeignKey(MilkTank, on_delete=models.CASCADE)
    name = models.ForeignKey('Worker', on_delete=models.CASCADE)
    liters = models.IntegerField("Число залитых литров")
    comment = models.CharField("Комментарий к заливке", max_length=50)
    date = models.DateField("Время заливки", auto_now=True)

    # подкласс для корректного вывода названий в админке
    class Meta:
        verbose_name = 'Заливка'
        verbose_name_plural = 'Заливки'


class Worker(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField('Имя рабочего', max_length=50)
    start_date = models.DateField('Дата приема на работу', auto_now=True)
    salary = models.IntegerField('Оклад')
    

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'