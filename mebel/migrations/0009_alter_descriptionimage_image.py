# Generated by Django 4.1.7 on 2023-04-30 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mebel', '0008_alter_descriptionimage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descriptionimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='desc_image', verbose_name='Картинка'),
        ),
    ]
