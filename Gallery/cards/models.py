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
        ('nature', 'Nature'),
        ('city', 'City'),
        ('cars', 'Cars'),
        ('animals', 'Animals'),
        ('Hi-Tech', 'Hi-Tech'),
        ('sport', 'Sport'),
        ('cosmos', 'Cosmos'),
        ('science', 'Science')
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/')
    title = models.CharField('Название', max_length=50, default='')
    rating = models.IntegerField('Рейтинг изображения')
    downloads = models.IntegerField('Количество скачиваний')
    tags = models.ManyToManyField(to=Tag, blank=True)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    category = models.CharField(choices=categories, max_length=30)

    # методы моделей
    # def __str__(self):
    #     # return f'{str(self.image)[7:]} от {str(self.date)[:16]}'
    #     return f'{str(self.title)} от {str(self.date)[:16]}'
    # print('image---------------', image)

    def get_absolute_url(self):
        return f'/{self.category}/{self.id}'

    class Meta:
        ordering = ['date', 'rating']

    def tag_list(self):
        s = ''
        for t in self.tags.all():
            s += t.title + ' '
        return s
