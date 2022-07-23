from django.shortcuts import render

from allauth.account.forms import LoginForm, SignupForm


def landing(request):
    form = LoginForm()
    return render(request, 'index.html', {'form': form, 'title': 'Welcome'})


def load_login_form(request):
    form = LoginForm()
    return render(request, 'allauth/account/login.html', {'form': form})

def load_register_form(request):
    form = SignupForm()
    return render(request, 'allauth/account/signup.html', {'form': form})