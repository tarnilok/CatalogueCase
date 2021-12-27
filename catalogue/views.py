from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.serializers import Serializer
from .serializers import CategorySerializer, ProductSerializer, SliderSerializer, FavouriteSerializer
from .models import Favourite, Slider, Category, Product
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly, IsUserOrNotAllowed
from rest_framework import status

class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    
class CategoryWithDescriptionView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, format=None, **kwargs):
        queryset = Category.objects.filter(id = kwargs['id'])
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
    
class ProductView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, format=None, **kwargs):
        is_id = Category.objects.filter(name=kwargs['category'])
        if kwargs['id'] == is_id[0].id : categoryName = Product.objects.filter(category__name=kwargs['category'])
        serializer = ProductSerializer(categoryName, many=True)
        return Response(serializer.data)
    
class OnlyProductsView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    
class SliderView(ListCreateAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    permission_classes = [IsAdminOrReadOnly]
    
class FavouriteViews(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    permission_classes = [IsUserOrNotAllowed]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        data = Product.objects.get(name=instance.productId)
        data.isFavorite = False
        data.save()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)





