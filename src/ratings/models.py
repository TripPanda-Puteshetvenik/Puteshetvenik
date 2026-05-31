from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Rating(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Цена')
    location = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Локация')
    atmosphere = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Атмосфера')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['post', 'user']
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return f'Оценка от {self.user.username} за {self.post.title}'

    @property
    def average(self):
        return round((self.price + self.location + self.atmosphere) / 3, 1)
