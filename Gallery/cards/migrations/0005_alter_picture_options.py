# Generated by Django 4.2.7 on 2023-12-02 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_alter_picture_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='picture',
            options={'ordering': ['date', 'rating']},
        ),
    ]