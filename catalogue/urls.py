from django.db import router
from django.urls import path, include
from .views import ProductView, SliderView, CategoryView, OnlyProductsView, FavouriteViews, ProductWithIsFavouriteView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', OnlyProductsView)
router.register('favorite', FavouriteViews)
router.register('categories', CategoryView)

urlpatterns = [
    path('categories/<int:id>/products/', ProductView.as_view()),
    path('products/<int:id>/', ProductWithIsFavouriteView.as_view()),
    path('sliders/', SliderView.as_view()),
    path('', include(router.urls)),
]