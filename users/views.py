from django.views.generic import FormView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from .models import User
from .mixins import LoggedOutOnlyView
from .forms import LoginForm


class LoginView(FormView):

    template_name = 'users/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        next_arg = self.request.GET.get('next')
        if next_arg is not None:
            return next_arg
        else:
            return reverse('core:home')
