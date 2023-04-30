from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token
from main.views import UserListAPIView, CategoryListAPIView, RolesListAPIView, ItemListAPIView, BasketListAPIView, CommentsListAPIView, RatingsListAPIView, DeliveryListAPIView, user_detail, roles_detail, category_detail, item_detail, basket_detail, comments_detail, ratings_detail, delivery_detail


urlpatterns = [
    path('login/', obtain_jwt_token),
    
    path('user/', UserListAPIView.as_view()),
    path('user/<int:product_id>/', UserListAPIView.as_view()),
    path('category/', CategoryListAPIView.as_view()),
    path('category/<int:product_id>/', CategoryListAPIView.as_view()),
    path('roles/', RolesListAPIView.as_view()),
    path('roles/<int:product_id>/', RolesListAPIView.as_view()),
    path('item/', ItemListAPIView.as_view()),
    path('item/<int:product_id>/', ItemListAPIView.as_view()),
    path('basket/', BasketListAPIView.as_view()),
    path('basket/<int:product_id>/', BasketListAPIView.as_view()),
    path('comments/', CommentsListAPIView.as_view()),
    path('comments/<int:product_id>/', CommentsListAPIView.as_view()),
    path('ratings/', RatingsListAPIView.as_view()),
    path('ratings/<int:product_id>/', RatingsListAPIView.as_view()),
    path('delivery/', DeliveryListAPIView.as_view()),
    path('delivery/<int:product_id>/', DeliveryListAPIView.as_view()),

]
