from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    header = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(verbose_name="Содержимое блога")
    image = models.ImageField(upload_to='blogs/', verbose_name='Превью', **NULLABLE)
    date_create = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    count_views = models.IntegerField(default=0, verbose_name="Количество просмотров")
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано', **NULLABLE)

    def __str__(self):
        return f'{self.header.title()}'

    class Meta:
        verbose_name = 'Блоговая запись'
        verbose_name_plural = 'Блоговые записи'
