from django import forms
from .models import Recipe

class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'cost','ingredients')
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple
        }