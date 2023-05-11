from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    name =  models.CharField(max_length=50)
    email = models.CharField(max_length = 300)
    password = models.CharField(max_length=50)
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

class Roles(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=300)
    def to_json(self):
        return {
            'id': self.id,
            'role': self.role
        }

class Category(models.Model):
    name =  models.CharField(max_length=50)
    description = models.TextField(default="")
    image_url = models.CharField(max_length=300)
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image_url': self.image_url,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class Item(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    description = models.TextField(default="")
    image_url = models.CharField(max_length=300)
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'image_url': self.image_url,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
#****************************************************************************************************
class Basket(models.Model):
    product_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def to_json(self):
        return {
            'id': self.id
        }

class Comments(models.Model):
    product_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default="")
    created_at = datetime.datetime.now()

    def to_json(self):
        return {
            'id': self.id,
            'description': self.description,
            'created_at': self.created_at
        }

class Ratings(models.Model):
    product_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    created_at = datetime.datetime.now()

    def to_json(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'created_at': self.created_at
        }


class Delivery(models.Model):
    product_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_company = models.CharField(max_length=300)
    description = models.TextField(default="")
    image_url = models.CharField(max_length=300)
    card_number = models.CharField(max_length=20)
    CSV = models.CharField(max_length=3)
    card_name = models.CharField(max_length=300)
    created_at = datetime.datetime.now()
    delivery_date = models.TextField(default="")
    street = models.CharField(max_length=300)
    home = models.CharField(max_length=5)
    appartment = models.CharField(max_length=5)

    def to_json(self):
        return {
            'id': self.id,
            'delivery_company': self.delivery_company,
            'description': self.description,
            'image_url': self.image_url,
            'created_at': self.created_at,
            'delivery_date': self.delivery_date,
            'card_number': self.card_number,
            'CSV': self.CSV,
            'card_name': self.card_name,
            'street': self.street,
            'home': self.home,
            'appartment': self.appartment,
            'product_id': self.product_id,
            'user_id': self.user_id
        }


