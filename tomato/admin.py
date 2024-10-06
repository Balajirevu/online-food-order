from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import  Restaurent,Menu

# Register your models here.
@register(Restaurent)
class Restaurentadmin(admin.ModelAdmin):
    list_display=['restaurent_name','restaurent_description','restaurent_address','restaurent_phone','restaurent_image',
                  'restaurent_rating','restaurent_delivery_charge','restaurent_cuisine','is_open']

@register(Menu)
class Menuadmin(admin.ModelAdmin):
    list_display=['item_name','item_price','item_description','item_image','item_category','is_available']