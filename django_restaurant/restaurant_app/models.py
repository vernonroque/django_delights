from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    cost = models.DecimalField(max_digits = 10, decimal_places = 2)
    
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length = 200)
    price_per_unit = models.DecimalField(max_digits = 10, decimal_places = 2)
    items_available = models.IntegerField()

    #recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
class Purchase(models.Model):
    item_purchased = models.CharField(max_length = 200)

    # I need to figure out how i can subtract ingredient items based off the
    # item purchased
