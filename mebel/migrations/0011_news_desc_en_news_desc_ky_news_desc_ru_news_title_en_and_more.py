# Generated by Django 4.1.7 on 2023-05-26 08:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mebel', '0010_alter_itemsfurniture_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='desc_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Текст новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='desc_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Текст новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='desc_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Текст новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ky',
            field=models.CharField(max_length=200, null=True, verbose_name='Новости'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Новости'),
        ),
    ]