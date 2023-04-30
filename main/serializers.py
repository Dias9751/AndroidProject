from rest_framework import serializers
from main.models import User, Category, Item, Roles, Basket, Comments, Ratings, Delivery


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')

class RolesSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Roles
        fields = ('id', 'role', 'user', 'user_id')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'image_url', 'created_at', 'updated_at')

class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Item
        fields = ('id', 'name', 'description', 'price', 'image_url', 'created_at', 'updated_at', 'category', 'categoty_id')

class BasketSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    item = ItemSerializer(read_only=True)
    item_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Basket
        fields = ('id', 'user', 'user_id', 'item', 'item_id')

class CommentsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    item = ItemSerializer(read_only=True)
    item_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Comments
        fields = ('id', 'description', 'created_at', 'user', 'user_id', 'item', 'item_id')

class RatingsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    item = ItemSerializer(read_only=True)
    item_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Ratings
        fields = ('id', 'rating', 'created_at,' 'user', 'user_id', 'item', 'item_id')

class DeliverySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    item = ItemSerializer(read_only=True)
    item_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Delivery
        fields = ('id', 'delivery_company', 'description', 'image_url',
        'created_at', 'delivery_date', 'card_number', 'CSV', 'card_name',
        'street', 'home', 'appartment', 'user', 'user_id', 'item', 'item_id')