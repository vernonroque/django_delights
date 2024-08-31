from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('login/', views.login_view, name="login"),
  path('recipe_create/', views.RecipeCreate.as_view() ,name="recipecreate"),
  path('recipe_list/',views.RecipeList.as_view(), name="recipelist"),
  path('recipe_update/<pk>',views.RecipeUpdate.as_view(), name="recipeupdate"),
  path('recipe_delete/<pk>',views.RecipeDelete.as_view(), name="recipedelete"),
  path('ingredient_list/',views.IngredientList.as_view(), name="ingredientlist"),
  path('ingredient_create/', views.IngredientCreate.as_view() ,name="ingredientcreate"),
  path('ingredient_update/<pk>',views.IngredientUpdate.as_view(), name="ingredientupdate"),
  path('ingredient_delete/<pk>',views.IngredientDelete.as_view(), name="ingredientdelete"),
  path('customer_purchase_list/',views.PurchaseList.as_view(), name="customerpurchaselist"),
  path('customer_purchase_create/', views.CustomerPurchaseCreate.as_view() ,name="customerpurchasecreate"),
  path('customer_purchase_update/<pk>',views.CustomerPurchaseUpdate.as_view(), name="customerpurchaseupdate"),
  path('customer_purchase_delete/<pk>',views.CustomerPurchaseDelete.as_view(), name="customerpurchasedelete"),

]