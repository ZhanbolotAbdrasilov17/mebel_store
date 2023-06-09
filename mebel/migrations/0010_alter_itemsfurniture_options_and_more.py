# Generated by Django 4.1.7 on 2023-04-30 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mebel', '0009_alter_descriptionimage_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemsfurniture',
            options={'verbose_name': 'Коллекция категорий', 'verbose_name_plural': 'Коллекция категорий'},
        ),
        migrations.RemoveField(
            model_name='itemsfurniture',
            name='item_1',
        ),
        migrations.RemoveField(
            model_name='itemsfurniture',
            name='item_2',
        ),
        migrations.RemoveField(
            model_name='itemsfurniture',
            name='item_3',
        ),
        migrations.RemoveField(
            model_name='itemsfurniture',
            name='item_4',
        ),
        migrations.RemoveField(
            model_name='itemsfurniture',
            name='item_5',
        ),
        migrations.RemoveField(
            model_name='itemsfurniture',
            name='item_6',
        ),
        migrations.AddField(
            model_name='itemsfurniture',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='desc_image', verbose_name='Картинка'),
        ),
        migrations.AddField(
            model_name='itemsfurniture',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название статистики'),
        ),
    ]
