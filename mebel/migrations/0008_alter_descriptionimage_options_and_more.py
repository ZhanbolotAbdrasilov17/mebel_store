# Generated by Django 4.1.7 on 2023-04-30 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mebel', '0007_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='descriptionimage',
            options={'verbose_name': 'Коллекция - картинки', 'verbose_name_plural': 'Коллекция - картинки'},
        ),
        migrations.RenameField(
            model_name='descriptionimage',
            old_name='image_1',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='descriptionimage',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='descriptionimage',
            name='image_3',
        ),
        migrations.AddField(
            model_name='descriptionimage',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название статистики'),
        ),
    ]