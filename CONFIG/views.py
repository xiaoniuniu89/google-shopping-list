from django.shortcuts import render

from allauth.account.forms import LoginForm, SignupForm


def landing(request):
    form = LoginForm()
    return render(request, 'index.html', {'form': form, 'title': 'Welcome'})
