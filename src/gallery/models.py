from django.db import models


class GalleryImage(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Снимка в галерия'
        verbose_name_plural = 'Снимки в галерия'

    def __str__(self):
        return f'Снимка #{self.id} за {self.post.title}'
