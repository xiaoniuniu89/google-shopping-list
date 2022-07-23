from django.urls import path
from.views import all_lists

urlpatterns = [
    path('', all_lists, name='shopping_list_all')
]
