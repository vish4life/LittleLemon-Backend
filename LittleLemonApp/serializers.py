from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MenuItem, Category, Cart, Order, OrderItem
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = ['title']
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=MenuItem
        fields=['title','price','featured','category','id']

# following is to override the djoser default behavior of showing only email and allowing only email update to the mentioned fields
class CustomUserRegistrationSerializer(BaseUserRegistrationSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields=['id','first_name','last_name','username','email','password']
        
        

class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cart
        fields=['id','menuitem','unit_price','quantity','price','user']
        read_only_fields = ['user', 'price','id']
    # create is a method which is default in serializer. to do any dynamic calculations or updates to data from the request,
    # we use validated_data object which stores the information from request
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['price'] = validated_data['unit_price'] * validated_data['quantity']
        return super().create(validated_data)

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['id','user','delivery_crew','status','total','date']
        read_only_fields=['user','delivery_crew','status','total','date']

class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['id','user','delivery_crew','status','total','date']
        read_only_fields=['user','status','total','date']

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['id','user','delivery_crew','status','total','date']
        read_only_fields=['user','delivery_crew','total','date']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=['order','menuitem','quantity','unit_price','price']