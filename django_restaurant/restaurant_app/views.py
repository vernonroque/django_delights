from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Recipe, Ingredient, Purchase
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import RecipeCreateForm

recipes = [{
    'recipe_name':'grilled cheese', 
    'cost':'4',
    'ingredients':['bread','cheese']}]

# Create your views here.
def home(request):
    context = {"name": "Jenkins","recipes":recipes}
    return render(request,"restaurant_app/home.html", context)

# def new_recipe(request):
#     context = {"recipes":recipes}
#     return render(request,"restaurant_app/new_recipe.html",context)

def new_ingredient(request):
    context = {"recipes":recipes}
    return render(request,"restaurant_app/new_ingredient.html",context)
def customer_purchase(request):
    context = {"recipes":recipes}
    return render(request,"restaurant_app/customer_purchase.html",context)

class RecipeList(ListView):
    model = Recipe
    template_name = 'restaurant_app/recipe_list.html'
    context_object_name = 'recipes'

class RecipeCreate(CreateView):
    model = Recipe
    template_name = "restaurant_app/recipe_create_form.html"
    fields = ["name", "description", "cost"]
    success_url = reverse_lazy('recipelist')

class RecipeUpdate(UpdateView):
    model = Recipe
    template_name = 'restaurant_app/recipe_update_form.html'
    fields = ["name", "description", "cost"]
    success_url = reverse_lazy('recipelist')

class RecipeDelete(DeleteView):
    model = Recipe
    template_name = 'restaurant_app/recipe_delete_form.html'
    success_url = reverse_lazy('recipelist')

#Another way to create a form with more customization
def new_recipe(request):
    if request.method == "POST":
        form = RecipeCreateForm(request.POST)
        # Add the form validation below:
        if form.is_valid():
            form.save()
            # messages.success(request, "Recipe created successfully!")
            return redirect('recipelist')
    else:
        form = RecipeCreateForm()

    return render(request, "restaurant_app/new_recipe.html", {"form":form})
