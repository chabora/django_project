"""Defindo padrão de URL para contas"""

from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # inclui URLs de autenticação default
    path('', include('django.contrib.auth.urls')),
    # página de cadastro
    path('register/', views.register, name='register'),
]
