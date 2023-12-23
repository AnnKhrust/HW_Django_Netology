from django.db import models

class Tags(models.Model):
    name = models.CharField(max_length=100, verbose_name='Тег')
    class Meta:
        ordering = ['-name']

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tags, through='Scopes')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scopes(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField()

    class Meta:
        ordering = ['-is_main']