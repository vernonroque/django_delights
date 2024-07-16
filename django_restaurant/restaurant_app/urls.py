from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('new_recipe/', views.new_recipe ,name="new_recipe"),
  path('new_ingredient/', views.new_ingredient, name="new_ingredient"),
  path('customer_purchase/', views.customer_purchase, name="customer_purchase"),
  path('recipe_list/',views.RecipeList.as_view(), name="recipelist")
]