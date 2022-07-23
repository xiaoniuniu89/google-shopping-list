from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ShoppingListItem(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name

class ShoppingList(models.Model):
    title = models.CharField(max_length=128, default="New List")
    user = models.ForeignKey(User, related_name='shopping_lists', on_delete=models.CASCADE)
    shopping_list_items = models.ManyToManyField(ShoppingListItem, related_name="shopping_items", blank=True)
    
    def __str__(self):
        return self.title