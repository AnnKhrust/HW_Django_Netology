from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название датчика')
    description = models.CharField(max_length=200, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements',
                                  verbose_name='Название датчика')
    temperature = models.FloatField(verbose_name='Температура')
    date = models.DateField(auto_now_add=True, verbose_name='Дата измерения')

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

    def __str__(self):
        return self.name