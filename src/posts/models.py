from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from categories.models import Country, TravelType


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Заглавие')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    cover_image = models.ImageField(upload_to='posts/covers/', blank=True, null=True)
    body = models.TextField(verbose_name='Съдържание')
    location_name = models.CharField(max_length=200, verbose_name='Локация')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    travel_types = models.ManyToManyField(TravelType, blank=True, related_name='posts', verbose_name='Типове пътуване')
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Пътепис'
        verbose_name_plural = 'Пътеписи'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            import uuid
            self.slug = slugify(self.title) or str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)

    def get_avg_rating(self):
        result = self.ratings.aggregate(
            avg_price=Avg('price'),
            avg_location=Avg('location'),
            avg_atmosphere=Avg('atmosphere'),
        )
        values = [v for v in result.values() if v is not None]
        if not values:
            return None
        return {
            'price': round(result['avg_price'] or 0, 1),
            'location': round(result['avg_location'] or 0, 1),
            'atmosphere': round(result['avg_atmosphere'] or 0, 1),
            'overall': round(sum(values) / len(values), 1),
            'count': self.ratings.count(),
        }
