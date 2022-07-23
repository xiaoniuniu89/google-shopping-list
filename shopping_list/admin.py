from django.contrib import admin
from .models import ShoppingList, ShoppingListItem

# Register models to appear in admin panel.
admin.site.register(ShoppingList)
admin.site.register(ShoppingListItem)