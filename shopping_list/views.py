from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import ShoppingListItem, ShoppingList
from django.contrib.auth.mixins import UserPassesTestMixin
from .utils import render_to_pdf
from django.views.generic import View
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
    
def update_title(request, list):
    list = get_object_or_404(ShoppingList, pk=list)
    if list.user == request.user:
        list.title = request.POST.get('title')
        list.save()
        return HttpResponse()
    
def clear_list(request, list):
    list = get_object_or_404(ShoppingList, pk=list)
    if list.user == request.user:
        list.shopping_list_items.clear()
        list.save()
        return render(request, 'shopping_list/partials/list_single.html', {'list': list})

def delete_list(request, list):
    list = get_object_or_404(ShoppingList, pk=list)
    if list.user == request.user:
        list.delete()
        shopping_lists = request.user.shopping_lists.all()
        return render(request, 'shopping_list/partials/lists.html', {'shopping_lists': shopping_lists})



class GenerateShoppingListPDF(UserPassesTestMixin, View):
    """generate a pdf shopping list"""

    def get(self, request, pk, *args, **kwargs):
        """ view to generate a pdf shopping list """
        list = get_object_or_404(ShoppingList, pk=pk)
        pdf = render_to_pdf('shopping_list/pdf_list.html',
                            {'list': list})
        return HttpResponse(pdf, content_type='application/pdf')

    def test_func(self):
        pk = self.kwargs['pk']
        return self.request.user == ShoppingList.objects.get(pk=pk).user
    
