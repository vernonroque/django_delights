from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('new_recipe/',views.new_recipe,name="new_recipe"),
  path('recipe_create/', views.RecipeCreate.as_view() ,name="recipecreate"),
  path('new_ingredient/', views.new_ingredient, name="new_ingredient"),
  path('customer_purchase/', views.customer_purchase, name="customer_purchase"),
  path('recipe_list/',views.RecipeList.as_view(), name="recipelist"),
  path('recipe_update/<pk>',views.RecipeUpdate.as_view(), name="recipeupdate"),
  path('recipe_delete/<pk>',views.RecipeDelete.as_view(), name="recipedelete")

]