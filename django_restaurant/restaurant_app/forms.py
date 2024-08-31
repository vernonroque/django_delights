from django import forms
from .models import Purchase, Recipe

class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'cost','ingredients')
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple
        }
        
class RecipeUpdateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'cost','ingredients')
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['item_purchased', 'recipe']  # Include the 'recipe' field
        widgets = {
            'recipe': forms.Select(),  # Ensure the recipe field is rendered as a dropdown menu
        }