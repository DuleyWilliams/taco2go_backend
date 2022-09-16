"""taco2go URL Configuration

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
from rest_framework import routers
from taco2goapi.views import MyBuiltTacoView
from taco2goapi.views import ProteinView
from taco2goapi.views import RatingView
from taco2goapi.views import SauceView
from taco2goapi.views import ShellView
from taco2goapi.views import ToppingView
from taco2goapi.views import RestaurantView
from taco2goapi.views import MyFavsView
from taco2goapi.views import TacoSauceView
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from taco2goapi.views import register_user, login_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'mybuilttacos', MyBuiltTacoView, 'mybuilttaco')
router.register(r'proteins', ProteinView, 'protein')
router.register(r'ratings', RatingView, 'rating')
router.register(r'sauces', SauceView, 'sauce')
router.register(r'shells', ShellView, 'shell')
router.register(r'toppings', ToppingView, 'topping')
router.register(r'restaurants', RestaurantView, 'restaurant')
router.register(r'myfavs', MyFavsView, 'myfav')
router.register(r'tacosauces', TacoSauceView, 'tacosauce')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
