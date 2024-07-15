from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Ingredient, Purchase
from django.views.generic import ListView
# from django.views.generic.edit import CreateView, DeleteView, UpdateView

recipes = [{
    'recipe_name':'grilled cheese', 
    'cost':'4',
    'ingredients':['bread','cheese']}]

# Create your views here.
def home(request):
    context = {"name": "Jenkins","recipes":recipes}
    return render(request,"restaurant_app/home.html", context)

def new_recipe(request):
    context = {"recipes":recipes}
    return render(request,"restaurant_app/new_recipe.html",context)

def new_ingredient(request):
    context = {"recipes":recipes}
    return render(request,"restaurant_app/new_ingredient.html",context)
def customer_purchase(request):
    context = {"recipes":recipes}
    return render(request,"restaurant_app/customer_purchase.html",context)

class RecipeList(ListView):
    model = Recipe
