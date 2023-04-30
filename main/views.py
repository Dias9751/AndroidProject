import json

from django.shortcuts import render, Http404
from django.http import HttpResponse

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from main.models import User, Category, Item, Roles, Basket, Comments, Ratings, Delivery
from main.serializers import UserSerializer, RolesSerializer, CategorySerializer, ItemSerializer, BasketSerializer, CommentsSerializer, RatingsSerializer, DeliverySerializer

# Create your views here.

class UserListAPIView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RolesListAPIView(APIView):
    def get(self, request):
        roles = Roles.objects.all()
        serializer = RolesSerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RolesSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryListAPIView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = UserSerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemListAPIView(APIView):
    def get(self, request):
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BasketListAPIView(APIView):
    def get(self, request):
        basket = Basket.objects.all()
        serializer = BasketSerializer(basket, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BasketSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentsListAPIView(APIView):
    def get(self, request):
        comments = Comments.objects.all()
        serializer = CommentsSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentsSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RatingsListAPIView(APIView):
    def get(self, request):
        ratings = Ratings.objects.all()
        serializer = UserSerializer(ratings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RatingsSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeliveryListAPIView(APIView):
    def get(self, request):
        delivery = Delivery.objects.all()
        serializer = DeliverySerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DeliverySerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def user_detail(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)

@csrf_exempt
def roles_detail(request, roles_id):
    try:
        roles = Roles.objects.get(role_id=roles_id)
    except Roles.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    serializer = RolesSerializer(roles)
    return JsonResponse(serializer.data)

@csrf_exempt
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    serializer = CategorySerializer(category)
    return JsonResponse(serializer.data)

@csrf_exempt
def item_detail(request, item_id):
    try:
        item = Item.objects.get(product_id=item_id)
    except Item.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    serializer = ItemSerializer(item)
    return JsonResponse(serializer.data)

@csrf_exempt
def basket_detail(request, basket_id):
    try:
        basket = Basket.objects.get(basket_id=basket_id)
    except Basket.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    serializer = BasketSerializer(basket)
    return JsonResponse(serializer.data)

@csrf_exempt
def comments_detail(request, comments_id):
    try:
        comments = Comments.objects.get(comment_id=comments_id)
    except Comments.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    serializer = CommentsSerializer(comments)
    return JsonResponse(serializer.data)

@csrf_exempt
def ratings_detail(request, ratings_id):
    try:
        ratings = Ratings.objects.get(rating_id=ratings_id)
    except Ratings.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    serializer = RatingsSerializer(ratings)
    return JsonResponse(serializer.data)

@csrf_exempt
def delivery_detail(request, delivery_id):
    try:
        delivery = Delivery.objects.get(delivery_id=delivery_id)
    except Delivery.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    serializer = DeliverySerializer(delivery)
    return JsonResponse(serializer.data)


#*********************************************************************************************
"""
class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer2(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    permission_classes = (IsAuthenticated,)"""
"""
@csrf_exempt
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = CategorySerializer2(category)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CategorySerializer2(instance=category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({'message': 'deleted'}, status=204)




@csrf_exempt
def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    serializer = ProductSerializer(product)
    return JsonResponse(serializer.data)

@csrf_exempt
def category_detail_product(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    produc = category.product_set.all()
    serializer = ProductSerializer(produc, many = True)
    return JsonResponse(serializer.data, safe = False)

@csrf_exempt
def restaurant_detail(request, restaurant_id):
    try:
        restaurant = Restaurant.objects.get(id=restaurant_id)
    except Restaurant.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    serializer = RestaurantSerializer(restaurant)
    return JsonResponse(serializer.data)

@csrf_exempt
def delivery_detail(request, delivery_id):
    try:
        delivery = Delivery.objects.get(id=delivery_id)
    except Delivery.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    serializer = DeliverySerializer(delivery)
    return JsonResponse(serializer.data)"""