from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Kategori)



class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('nama','judul','body','kategori','date')

admin.site.register(Artikel, ArtikelAdmin)

# class ResepAdmin(admin.ModelAdmin):
#     list_display = ('idMeal','strMeal','strDrinkAlternate','strCategory','strArea', 'strInstructions', 'strTags','strYoutube','strIngredient1','strIngredient2','strIngredient3', 'strIngredient4', 'strIngredient5', 'strIngredient6', 'strIngredient7', 'strIngredient8', 'strIngredient9', 'strIngredient10', 'strIngredient11', 'strIngredient12', 'strIngredient13', 'strMeasure1', 'strMeasure2', 'strMeasure3', 'strMeasure4', 'strMeasure5', 'strMeasure6', 'strMeasure7', 'strMeasure8', 'strMeasure9', 'strMeasure10', 'strMeasure11', 'strMeasure12', 'strMeasure13', 'strSource', 'strImageSource', 'strCreativeCommonsConfirmed', 'dateModified', 'strMealThumb')
# admin.site.register(Resep, ResepAdmin)