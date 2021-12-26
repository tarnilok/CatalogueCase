from rest_framework import fields, serializers
from .models import Category, Product, Slider, Favourite

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']
        
class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = '__all__'
        
class SliderSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)
    class Meta:
        model = Slider
        fields = ['productId', 'image']
        
    def create(self, validated_data):
        # print('vvvvvvvvvvvv:', validated_data)
        # if (validated_data['image']):
        image_data = validated_data.pop('image')
        # if (image_data):
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
        print('vvvvvvvvvvvv:', validated_data['productId'].id)
        data = Product.objects.get(id=validated_data['productId'].id)
        data.isFavorite = True
        data.save()
        favourite = Favourite.objects.create(**validated_data)
        favourite.save()
        return favourite
    
    # def get(self, obj):
    #     return Favourite.objects.filter(productId_isFavorite=True)