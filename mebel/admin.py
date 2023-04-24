from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.


@admin.register(FurnitureCategory)
class FurnitureCategoryAdminList(admin.ModelAdmin):
    pass

@admin.register(Furniture)
class FurnitureAdminList(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_display_links = ('title', 'category')
    search_fields = ('title', 'category__title')


@admin.register(Partner)
class PartnerAdminList(admin.ModelAdmin):
    pass


@admin.register(Email)
class EmailAdminList(admin.ModelAdmin):
    list_display = ('address', 'id')
    list_display_links = ('address', 'id')
    search_fields = ('address', 'id')