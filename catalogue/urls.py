from django.db import router
from django.urls import path, include
from .views import ProductView, SliderView, CategoryView, CategoryWithDescriptionView, OnlyProductsView, FavouriteViews
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', OnlyProductsView)

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('categories/<int:id>/', CategoryWithDescriptionView.as_view()),
    path('categories/<int:id>/<str:category>/', ProductView.as_view()),
    path('', include(router.urls)),
    path('sliders/', SliderView.as_view()),
    path('favourites/', FavouriteViews.as_view()),
]