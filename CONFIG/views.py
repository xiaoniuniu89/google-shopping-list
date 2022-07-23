from django.shortcuts import render, redirect

from allauth.account.forms import LoginForm, SignupForm


def landing(request):
    if request.user.is_authenticated:
        return redirect('shopping_list_all')
    form = LoginForm()
    return render(request, 'index.html', {'form': form, 'title': 'Welcome'})
