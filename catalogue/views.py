from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.serializers import Serializer
from .serializers import CategorySerializer, ProductSerializer, SliderSerializer, FavouriteSerializer
from .models import Favourite, Slider, Category, Product
from rest_framework.response import Response

class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryWithDescriptionView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    def get(self, request, format=None, **kwargs):
        queryset = Category.objects.filter(id = kwargs['id'])
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
    
class ProductView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get(self, request, format=None, **kwargs):
        is_id = Category.objects.filter(name=kwargs['category'])
        if kwargs['id'] == is_id[0].id : categoryName = Product.objects.filter(category__name=kwargs['category'])
        serializer = ProductSerializer(categoryName, many=True)
        return Response(serializer.data)
    
class OnlyProductsView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class SliderView(ListCreateAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    
class FavouriteViews(ListCreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    
    # def get(self, request, *args, **kwargs):
    #     favourites = Product.objects.filter(isFavorite=True)
    #     serializer = FavouriteSerializer(favourites, many=True)
    #     return Response(serializer.data)





