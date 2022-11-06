from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Публикация')
    content = models.TextField(blank=True, verbose_name='Содержимое')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='photos/%y/%m/%d/', verbose_name='Картинка', blank=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликована')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-created_at','title']