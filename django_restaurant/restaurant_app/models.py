from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    cost = models.DecimalField(max_digits = 10, decimal_places = 2)
    created_at = models.DateTimeField(auto_now_add=True)  # Set on creation
    updated_at = models.DateTimeField(auto_now=True)      # Set on each save
    
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length = 200)
    price_per_unit = models.DecimalField(max_digits = 10, decimal_places = 2)
    items_available = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # Set on creation
    updated_at = models.DateTimeField(auto_now=True)      # Set on each save

    #recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
class Purchase(models.Model):
    item_purchased = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)  # Set on creation
    updated_at = models.DateTimeField(auto_now=True)      # Set on each save

class Recipe_Ingredient(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('recipe_id', 'ingredient_id'))

    # I need to figure out how i can subtract ingredient items based off the
    # item purchased