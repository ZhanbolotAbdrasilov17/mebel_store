from django.db import models

# Create your models here.

class FurnitureCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название категории',)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории мебели'
        verbose_name = 'Категория мебели'


class Furniture(models.Model):
    category = models.ForeignKey(FurnitureCategory, on_delete=models.CASCADE, verbose_name='Категория мебели',
                                 related_name='category_furniture')
    title = models.CharField(max_length=200, verbose_name='Название мебели')
    # text = RichTextField(verbose_name='Текст', blank=True, null=True, )
    image = models.ImageField(upload_to='partner-image', blank=True, null=True, verbose_name='Картинка мебели')
    price = models.CharField(max_length=200, verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Партнёры'
        verbose_name = 'Партнёр'