from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.


@admin.register(FurnitureCategory)
class FurnitureCategoryAdminList(admin.ModelAdmin):
    pass

@admin.register(Furniture)
class FurnitureAdminList(admin.ModelAdmin):
    pass


@admin.register(Partner)
class PartnerAdminList(admin.ModelAdmin):
    pass
