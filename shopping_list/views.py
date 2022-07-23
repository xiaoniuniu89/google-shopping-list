from django.shortcuts import get_object_or_404, render
from .models import ShoppingListItem, ShoppingList
# Create your views here.


def all_lists(request):
    shopping_lists = request.user.shopping_lists.all()
    return render(request, 'shopping_list/main.html', {'shopping_lists': shopping_lists})



# htmx views 

def new_list(request):
    ShoppingList.objects.create(user=request.user)
    shopping_lists = request.user.shopping_lists.all()
    return render(request, 'shopping_list/partials/lists.html', {'shopping_lists': shopping_lists})

def remove_item(request, list, item):
    list = get_object_or_404(ShoppingList, pk=list)
    item = get_object_or_404(ShoppingListItem, pk=item)
    if list.user == request.user:
        list.shopping_list_items.remove(item)
        return render(request, 'shopping_list/partials/list_single.html', {'list': list})
    
def add_item(request, list):
    list = get_object_or_404(ShoppingList, pk=list)
    if list.user == request.user:
        item = ShoppingListItem.objects.get_or_create(name=request.POST.get('item'))[0]
        list.shopping_list_items.add(item)
        return render(request, 'shopping_list/partials/list_single.html', {'list': list})
