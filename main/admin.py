from django.contrib import admin

# Register your models here.

from main.models import User, Category, Item, Roles, Basket, Comments, Ratings, Delivery


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'image_url', 'created_at', 'updated_at']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'image_url', 'created_at', 'updated_at']

class RolesAdmin(admin.ModelAdmin):
    list_display = ['id', 'role']

class BasketAdmin(admin.ModelAdmin):
    list_display = ['id']

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'created_at']

class RatingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'rating', 'created_at']

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['id', 'delivery_company', 'description', 'image_url',
        'created_at', 'delivery_date', 'card_number', 'CSV', 'card_name',
        'street', 'home', 'appartment']

admin.site.register(User,  UserAdmin)
admin.site.register(Roles, RolesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Comments,  CommentsAdmin)
admin.site.register(Ratings, RatingsAdmin)
admin.site.register(Basket, BasketAdmin)
admin.site.register(Delivery, DeliveryAdmin)