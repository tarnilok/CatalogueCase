from rest_framework import serializers
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
    favourites = serializers.BooleanField(default=False)
    class Meta:
        model = Product
        fields = ['category', 'name', 'product_image', 'description', 'price', 'favourites']
        
class ProductWithIsFavouriteSerializer(serializers.ModelSerializer):
    favourites = serializers.BooleanField(default=False)
    class Meta:
        model = Product
        fields = ['category', 'name', 'product_image', 'description', 'price', 'favourites']

class SliderSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)
    class Meta:
        model = Slider
        fields = ['productId', 'image']
        
    def create(self, validated_data):
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
