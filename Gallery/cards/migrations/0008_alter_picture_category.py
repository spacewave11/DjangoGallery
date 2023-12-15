# Generated by Django 4.2.7 on 2023-12-11 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_picture_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='category',
            field=models.CharField(choices=[('nature', 'Nature'), ('city', 'City'), ('cars', 'Cars'), ('animals', 'Animals'), ('Hi-Tech', 'Hi-Tech'), ('sport', 'Sport'), ('cosmos', 'Cosmos'), ('science', 'Science'), ('minimalism', 'Minimalism')], max_length=30),
        ),
    ]