from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Restaurent(models.Model):
    restaurent_id=models.IntegerField(primary_key=True)
    restaurent_name=models.CharField(max_length=30)
    restaurent_description=models.TextField()
    restaurent_address=models.CharField(max_length=100)
    restaurent_phone=models.CharField(max_length=100)
    restaurent_image=models.ImageField(upload_to='restaurent_images/')
    restaurent_rating=models.FloatField()
    restaurent_delivery_charge=models.FloatField()
    restaurent_cuisine=models.CharField(max_length=50)
    is_open=models.BooleanField()

    def __str__(self):
        return self.restaurent_name

class Menu(models.Model):
    menu_id=models.IntegerField(primary_key=True)
    restaurent=models.ForeignKey(Restaurent,on_delete=models.CASCADE)
    item_name=models.CharField(max_length=30)
    item_price=models.FloatField()
    item_description=models.CharField(max_length=100)
    item_image=models.ImageField(upload_to='menu_images/')
    item_category=models.CharField(max_length=30)
    is_available=models.BooleanField()
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return self.item_name

class New_user(User):
    user_phone=models.CharField(max_length=30)
    user_address=models.CharField(max_length=100)


    def __str__(self):
        return self.username
    
class Order(models.Model):
    order_id=models.IntegerField(primary_key=True)
    user=models.ForeignKey(New_user,on_delete=models.CASCADE)
    restaurent=models.ForeignKey(Restaurent,on_delete=models.CASCADE)
    items=models.ManyToManyField(Menu)
    total_amount=models.FloatField()
    delivery_address=models.CharField(max_length=100)
    order_status=models.CharField(max_length=30)
    order_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order:{self.order_id}"


class CartItem(models.Model):
	menu= models.ForeignKey(Menu, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=0)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.quantity} x {self.menu.item_name}'

