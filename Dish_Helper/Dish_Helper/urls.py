"""Dish_Helper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path


from Dish_Helper_app.views import MainPageView, AddMealView, AddTypeOfMealView, AddIngredientView, \
    AddIngredientMeasurementView, ProfileRegisterView, MealDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name='base'),
    path('login/', auth_views.LoginView.as_view(template_name='templates/Dish_Helper_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='templates/Dish_Helper_app/logout.html'), name='logout'),
    path('register/', ProfileRegisterView.as_view(), name='register'),
    path('add_meal/', AddMealView.as_view(template_name='templates/Dish_Helper_app/meal_form.html'), name='add_meal'),
    path('add_type/', AddTypeOfMealView.as_view(), name='add_type'),
    path('add_ingredient/', AddIngredientView.as_view(), name='add_ingredient'),
    path('add_measurement/', AddIngredientMeasurementView.as_view(), name='add_measurement'),
    path('mealdetail/<int:id>/', MealDetailView.as_view(), name='mealdetail'),
]
