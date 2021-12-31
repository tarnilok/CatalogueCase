from rest_framework import serializers
from rest_framework.fields import NullBooleanField
from .models import Category, Product, Slider, Favourite

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        
class ProductSerializerWithoutFavourite(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    isFavorite = serializers.BooleanField(default=False)
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'product_image', 'description', 'price', 'isFavorite']
            
class SliderSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model = Slider
        fields = ['productId', 'image']
        
    def create(self, validated_data):
        if 'image' in validated_data:
            image_data = validated_data.pop('image')
            data = Product.objects.get(id=validated_data['productId'].id)
            data.product_image = image_data
            data.save()
        slider = Slider.objects.create(**validated_data)
        slider.save()
        return slider
              
class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'
        
    def create(self, validated_data):
        favourites = Favourite.objects.all()
        for fav in favourites:
            if fav.productId.id == validated_data['productId'].id and fav.user.id == validated_data['user'].id:
                raise serializers.ValidationError({"detail": "same field exists"})
        new_fav = Favourite.objects.create(**validated_data)
        new_fav.save()
        return new_fav
