from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.



class Logo(models.Model):
    logo = models.FileField(upload_to='logo', blank=True, null=True)

    def __str__(self):
        return 'Логотип'


    class Meta:
        verbose_name_plural = 'Логотип'
        verbose_name = 'Логотип'


class DescriptionImage(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название статистики', blank=True, null=True)
    image = models.ImageField(upload_to='desc_image', blank=True, null=True, verbose_name='Картинка')



    def __str__(self):
        return f'Коллекция {self.id}'

    class Meta:
        verbose_name_plural = 'Коллекция - картинки'
        verbose_name = 'Коллекция - картинки'


class ItemsFurniture(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название статистики', blank=True, null=True)
    image = models.ImageField(upload_to='desc_image', blank=True, null=True, verbose_name='Картинка')

    def __str__(self):
        return f'Коллекция {self.id}'

    class Meta:
        verbose_name_plural = 'Коллекция категорий'
        verbose_name = 'Коллекция категорий'


class FurnitureCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название категории',)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Категории мебели'
        verbose_name = 'Категория мебели'


class Furniture(models.Model):
    STATUS = (
        ('new', 'new'),
        ('sale', 'sale'),
        ('old', 'old')
    )
    status = models.CharField(choices=STATUS, max_length=4)
    category = models.ForeignKey(FurnitureCategory, on_delete=models.CASCADE, verbose_name='Категория мебели',
                                 related_name='category_furniture')
    title = models.CharField(max_length=200, verbose_name='Название мебели')
    desc = RichTextField(verbose_name='Описание')
    image_1 = models.ImageField(upload_to='partner-image', blank=True, null=True, verbose_name='Первая картинка')
    image_2 = models.ImageField(upload_to='partner-image', blank=True, null=True, verbose_name='Вторая картинка')
    price = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Мебель'
        verbose_name = 'Мебель'


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Новости")
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="news")
    desc = RichTextField(verbose_name='Текст новости')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        ordering = ['title']


class Reviews(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    image = models.ImageField(null=True, blank=True, upload_to="reviews")
    text = models.TextField(verbose_name="отзывы")
    position = models.CharField(max_length=200, blank=True, null=True, verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзывы'
        ordering = ['name']


class Partner(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название партнёра')
    image = models.ImageField(upload_to='partner-image', blank=True, null=True, verbose_name='Логотип партнера')
    link = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ссылка на сайт партнера')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Партнёры'
        verbose_name = 'Партнёр'


class Contact(models.Model):
    contacts = RichTextField(verbose_name='Контакты')
    email = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    whatsapp = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    vk = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return 'Контакты'

    class Meta:
        verbose_name_plural = 'Контакты'
        verbose_name = 'Контакты'


class Email(models.Model):
    address = models.CharField(max_length=200, verbose_name='Почта клиентов')


    class Meta:
        verbose_name_plural = 'Почтовые адреса'
        verbose_name = 'Почтовые адреса'
