# Generated by Django 4.2.7 on 2023-12-23 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0011_picture_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='category',
            field=models.CharField(choices=[('nature', 'Природа'), ('city', 'Город'), ('cars', 'Машины'), ('animals', 'Животные'), ('Hi-Tech', 'Hi-Tech'), ('sport', 'Спорт'), ('cosmos', 'Космос'), ('science', 'Наука'), ('minimalism', 'Минимализм'), ('new year', 'Новый год')], max_length=30),
        ),
    ]
