from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    
    def __str__(self):
         return self.nama
    
    class meta :
        verbose_name_plural = "Kategori"

class Artikel(models.Model):
    nama = models.CharField(max_length=100,blank=True,null=True)
    judul = models.CharField(max_length=100)
    body = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)
    
    class meta :
        ordering = ['-id']
        verbose_name_plural = "Artikel"

# class Resep(models.Model):
#     idMeal = models.CharField(max_length=1000,blank=True,null=True)
#     strMeal = models.CharField(max_length=1000,blank=True,null=True)
#     strDrinkAlternate = models.CharField(max_length=1000,blank=True,null=True)
#     strCategory = models.CharField(max_length=1000,blank=True,null=True)
#     strArea = models.CharField(max_length=1000,blank=True,null=True)
#     strInstructions = models.CharField(max_length=1000,blank=True,null=True)
#     strTags = models.CharField(max_length=1000,blank=True,null=True)
#     strYoutube = models.CharField(max_length=1000,blank=True,null=True)
#     strIngredient1 = models.CharField(max_length=1000,blank=True,null=True)
#     strIngredient2 = models.CharField(max_length=1000,blank=True,null=True)
#     strIngredient3 = models.CharField(max_length=1000,blank=True,null=True)
#     strIngredient4 = models.CharField(max_length=1000,blank=True,null=True)
#     strIngredient5 = models.CharField(max_length=1000,blank=True,null=True)
#     strIngredient6 = models.CharField(max_length=1000,blank=True,null=True)
#     strIngredient7 = models.CharField(max_length=1000,blank=True,null=True)
#     strIngredient8 = models.CharField(max_length=1000,blank=True,null=True)
#     strIngredient9 = models.CharField(max_length=1000,blank=True,null=True)
#     strIngredient10 = models.CharField(max_length=1000,blank=True,null=True)
#     strIngredient11= models.CharField(max_length=1000,blank=True,null=True)
#     strIngredient12= models.CharField(max_length=1000,blank=True,null=True)
#     strIngredient13= models.CharField(max_length=1000,blank=True,null=True)
#     strMeasure1 = models.CharField(max_length=1000,blank=True,null=True)
#     strMeasure2 = models.CharField(max_length=1000,blank=True,null=True)
#     strMeasure3 = models.CharField(max_length=1000,blank=True,null=True)
#     strMeasure4 = models.CharField(max_length=1000,blank=True,null=True)
#     strMeasure5 = models.CharField(max_length=1000,blank=True,null=True)
#     strMeasure6 = models.CharField(max_length=1000,blank=True,null=True)
#     strMeasure7 = models.CharField(max_length=1000,blank=True,null=True)
#     strMeasure8 = models.CharField(max_length=1000,blank=True,null=True)
#     strMeasure9 = models.CharField(max_length=1000,blank=True,null=True)
#     strMeasure10 = models.CharField(max_length=1000,blank=True,null=True)
#     strMeasure11 = models.CharField(max_length=1000,blank=True,null=True)
#     strMeasure12 = models.CharField(max_length=1000,blank=True,null=True)
#     strMeasure13 = models.CharField(max_length=1000,blank=True,null=True)
#     strSource = models.CharField(max_length=1000,blank=True,null=True)
#     strImageSource = models.CharField(max_length=1000,blank=True,null=True)
#     strCreativeCommonsConfirmed = models.CharField(max_length=1000,blank=True,null=True)
#     dateModified = models.CharField(max_length=1000,blank=True,null=True)
#     strMealThumb = models.CharField(max_length=1000,blank=True,null=True)
    
#     def __str__(self):
#         return "{} - {}".format(self.strMeal, self.strCategory)