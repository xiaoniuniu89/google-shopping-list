from django.urls import path
from.views import (
    all_lists,
    new_list,
    remove_item,
    add_item,
    update_title,
    clear_list,
    delete_list,
    GenerateShoppingListPDF
)

urlpatterns = [
    path('', all_lists, name='shopping_list_all')
]


htmx_urlpatterns = [
    path('new-list', new_list, name='new_list'),
    path('add-item/<int:list>/', add_item, name='add_item'),
    path('remove-item/<int:list>/<int:item>/', remove_item, name='remove_item'),
    path('update-list/<int:list>/', update_title, name='update_title'),
    path('clear-list/<int:list>/', clear_list, name='clear_list'),
    path('delete-list/<int:list>/', delete_list, name='delete_list'),
    path('pdf-shopping-list/<int:pk>/', GenerateShoppingListPDF.as_view(), name='make_pdf'),
]


urlpatterns += htmx_urlpatterns