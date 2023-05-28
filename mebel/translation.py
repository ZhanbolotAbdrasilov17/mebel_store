from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Furniture)
class FurnitureTranslation(TranslationOptions):
    fields = ('title',)

@register(FurnitureCategory)
class FurnitureCategoryTranslation(TranslationOptions):
    fields = ('title',)

@register(Partner)
class PartnerTranslation(TranslationOptions):
    fields = ('title',)

@register(News)
class NewsTranslation(TranslationOptions):
    fields = ('title', 'desc')