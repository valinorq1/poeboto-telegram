from django.contrib.auth import views as auth_views, login, authenticate, get_user_model
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse, Http404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.views import generic
from django.urls import reverse_lazy, path

from service import models
from .forms import *

User = get_user_model()


class AccountView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'users/account.html'

    def get_object(self):
        return self.request.user

class AccountActiveView(LoginRequiredMixin, generic.ListView):
    template_name = 'users/account.html'
    def get_queryset(self):
        return User.objects.all()
    

class AccountCartView(LoginRequiredMixin, generic.ListView):
    template_name = 'users/account.html'
    def get_queryset(self):
        return User.objects.all()

class RegisterView(generic.FormView):
    form_class = RegisterUserForm
    template_name = 'users/signup.html'
    logged_in_regirect_url = reverse_lazy('login')

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = User.objects.create(
                email=form.cleaned_data['email'],
                password=make_password(form.cleaned_data['password1'])
            )
            login(request, user)
        else:
            return render(request, self.template_name, {'form': form})

        return redirect('login')


class LoginView(View):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    logged_in_regirect_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            if not (user := authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])):
                form.add_error(field='email', error='Incorrect Email or Password')
                return render(request, self.template_name, {'form': form})

            login(request, user)

            if not form.cleaned_data['remember_me']:
                request.session.set_expiry(0)

        else:
            return render(request, self.template_name, {'form': form})

        return redirect('home')


class LogoutView(auth_views.LogoutView):
    pass

