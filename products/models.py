from pyexpat import model
from tkinter import CASCADE
from turtle import ondrag
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menu'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Drink(models.Model):
    category_id     = models.ForeignKey('Category', on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField

    class Meta:
        db_table = 'drinks'

class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'allergy'

class AllergyDrink(models.Model):
    allerg_id = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink_id = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_drink'

class Nut(models.Model):
    one_serving_kca = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    caffein_mg = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    allerg_id = models.ForeignKey('Allergy', on_delete=models.CASCADE,null=True)
    drink_id = models.ForeignKey('Drink', on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'nutritions'

class Img(models.Model):
    image_url = models.CharField(max_length=2000)
    drink_id = models.ForeignKey('Allergy', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Size(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45, null=True)
    size_fluid_ounce = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'sizes'
    


    