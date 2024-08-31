from django.db import models
from django.db.models import F

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length = 200)
    price_per_unit = models.DecimalField(max_digits = 10, decimal_places = 2)
    items_available = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # Set on creation
    updated_at = models.DateTimeField(auto_now=True)      # Set on each save

    def __str__(self):
        return self.name  # This ensures the name is used in the representation

class Recipe(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField()
    cost = models.DecimalField(max_digits = 10, decimal_places = 2)
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Set on creation
    updated_at = models.DateTimeField(auto_now=True)      # Set on each save
    
    def __str__(self):
        return self.name

class Purchase(models.Model):
    item_purchased = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)  # Set on creation
    updated_at = models.DateTimeField(auto_now = True)      # Set on each save
    recipe = models.ForeignKey(Recipe, null = True, on_delete = models.CASCADE)  # Foreign key to Recipe

    def save(self, *args, **kwargs):
        # Subtract ingredients when a purchase is saved
        ingredients = self.recipe.ingredients.all()  # Assuming recipe has a many-to-many relationship with ingredients
        for ingredient in ingredients:
            print(f"Before: {ingredient.name} has {ingredient.items_available} items available.")
            ingredient.items_available = F('items_available') - 1  # Subtract 1, adjust as needed
            ingredient.save()
            ingredient.refresh_from_db()
            print(f"After: {ingredient.name} has {ingredient.items_available} items available.")

        super().save(*args, **kwargs)

class Recipe_Ingredient(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete = models.CASCADE)

    class Meta:
        unique_together = (('recipe_id', 'ingredient_id'))

    # I need to figure out how i can subtract ingredient items based off the
    # item purchased