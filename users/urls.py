from django.urls import path, re_path, include

from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sign-up/', RegisterView.as_view(), name='sign-up'),

    path('account/', AccountView.as_view(), name='account'),
    path('account/active', AccountActiveView.as_view(), name='account-active'),
    path('account/cart', AccountCartView.as_view(), name='account-cart')
]