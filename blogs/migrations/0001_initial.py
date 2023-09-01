# Generated by Django 4.2.3 on 2023-08-15 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержимое блога')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogs/', verbose_name='Превью')),
                ('date_create', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('count_views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Блоговая запись',
                'verbose_name_plural': 'Блоговые записи',
            },
        ),
    ]