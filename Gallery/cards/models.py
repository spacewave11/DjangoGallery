from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    title = models.CharField(max_length=80)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Picture(models.Model):
    categories = (
        ('nature', 'Природа'),
        ('city', 'Город'),
        ('cars', 'Машины'),
        ('animals', 'Животные'),
        ('Hi-Tech', 'Hi-Tech'),
        ('sport', 'Спорт'),
        ('cosmos', 'Космос'),
        ('science', 'Наука'),
        ('minimalism', 'Минимализм'),
        ('new year', 'Новый год'),
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/')
    title = models.CharField('Название', max_length=50, default='')
    rating = models.IntegerField('Rating')  # Рейтинг изображения
    downloads = models.IntegerField('Скачали')  # Количество скачиваний
    tags = models.ManyToManyField(to=Tag, blank=True)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    category = models.CharField(choices=categories, max_length=30)
    is_verified = models.BooleanField('Проверено', default=False)

    def get_absolute_url(self):
        return f'/{self.category}/{self.id}'

    class Meta:
        ordering = ['date', 'rating']

    def tag_list(self):
        s = ''
        for t in self.tags.all():
            s += t.title + ' '
        return s
