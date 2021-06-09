from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from enum import Enum
from typing import Any, Dict

from .forms import RegisterUserForm


# Create your views here.
class MRQST(Enum):
    POSTING = 'POST'
    GETTING = 'GET'
    PATHCING = 'PATCH'


def register(request):
    if request.method == MRQST.POSTING.name:
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            login(request, new_user)
            return HttpResponseRedirect('/?account=success')
    form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})


class LoginToLogout(LoginView):
    template_name = 'users/login.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update({
            'message': 'Successfully logged out!',
            'tag': 'success'
        })
        return context


def logouting(request):
    logout(request)
    return LoginToLogout.as_view()(request)
