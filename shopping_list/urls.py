from django.urls import path
from.views import (
    all_lists,
    new_list,
    remove_item
)

urlpatterns = [
    path('', all_lists, name='shopping_list_all')
]


htmx_urlpatterns = [
    path('new-list', new_list, name='new_list'),
    path('remove-item/<int:list>/<int:item>/', remove_item, name='remove_item')
]


urlpatterns += htmx_urlpatterns