from django.shortcuts import render

# Create your views here.


def all_lists(request):
    return render(request, 'shopping_list/main.html', {})