from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .serializers import CategorySerializer, ProductSerializer, SliderSerializer, FavouriteSerializer, ProductWithIsFavouriteSerializer, ProductSerializerWithoutFavourite
from .models import Favourite, Slider, Category, Product
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly, IsAuthenticatedOrReadOnly

class CategoryView(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    
class ProductView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, format=None, **kwargs):
        categoryName = Product.objects.filter(category=kwargs['id'])
        serializer = ProductSerializer(categoryName, many=True)
        return Response(serializer.data)
    
class OnlyProductsView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerWithoutFavourite
    permission_classes = [IsAdminOrReadOnly]
    
class ProductWithIsFavouriteView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWithIsFavouriteSerializer
    
    def get(self, request, *args, **kwargs):
        product = Product.objects.filter(id = kwargs['id'])
        serializer = ProductWithIsFavouriteSerializer(product, many=True)
        return Response(serializer.data)
class SliderView(ListCreateAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    permission_classes = [IsAdminOrReadOnly]
    
class FavouriteViews(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


