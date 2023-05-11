from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token
from main.views import UserListAPIView, CategoryListAPIView, RolesListAPIView, ItemListAPIView, BasketListAPIView, CommentsListAPIView, RatingsListAPIView, DeliveryListAPIView, user_detail, roles_detail, category_detail, item_detail, basket_detail, comments_detail, ratings_detail, delivery_detail


urlpatterns = [
    path('login/', obtain_jwt_token),
    
    path('user/', UserListAPIView.as_view()),
    path('user/<int:user_id>/', user_detail),
    path('category/', CategoryListAPIView.as_view()),
    path('category/<int:category_id>/', category_detail),
    path('roles/', RolesListAPIView.as_view()),
    path('roles/<int:role_id>/', roles_detail),
    path('item/', ItemListAPIView.as_view()),
    path('item/<int:item_id>/', item_detail),
    path('basket/', BasketListAPIView.as_view()),
    path('basket/<int:basket_id>/', basket_detail),
    path('comments/', CommentsListAPIView.as_view()),
    path('comments/<int:comments_id>/', comments_detail),
    path('ratings/', RatingsListAPIView.as_view()),
    path('ratings/<int:ratings_id>/', ratings_detail),
    path('delivery/', DeliveryListAPIView.as_view()),
    path('delivery/<int:delivery_id>/', delivery_detail),

]
