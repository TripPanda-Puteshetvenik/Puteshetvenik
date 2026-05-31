from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length=100, verbose_name='Континент')
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=50, default='🌍')

    class Meta:
        verbose_name = 'Континент'
        verbose_name_plural = 'Континенти'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Държава')
    slug = models.SlugField(unique=True)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, related_name='countries')
    flag = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name = 'Държава'
        verbose_name_plural = 'Държави'
        ordering = ['name']

    def __str__(self):
        return self.name


class TravelType(models.Model):
    TRAVEL_TYPES = [
        ('extreme', 'Екстремно'),
        ('family', 'Семейно'),
        ('budget', 'Бюджетно'),
        ('luxury', 'Луксозно'),
        ('adventure', 'Приключенско'),
        ('cultural', 'Културно'),
        ('beach', 'Плажно'),
        ('mountain', 'Планинско'),
    ]
    name = models.CharField(max_length=50, choices=TRAVEL_TYPES, unique=True)
    icon = models.CharField(max_length=50, default='✈️')

    class Meta:
        verbose_name = 'Тип пътуване'
        verbose_name_plural = 'Типове пътувания'

    def __str__(self):
        return self.get_name_display()
