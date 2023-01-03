"""primeiro_projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from app_projeto.views import Home
from app_projeto.views import Ola
from app_projeto.views import Contato
from app_projeto.views import ListarPessoas
from app_projeto.views import SalvarPessoa

urlpatterns = [
    path('paginas/historia', TemplateView.as_view(template_name="historia.html"),name='historia'),
    path('', Home.as_view(),name='home'),
    path('diga-ola-para:<str:nome>/<str:cidade>', Ola.as_view(), name='oi'),
    path('contato', Contato.as_view(),name='contato'),
    path('sucesso', TemplateView.as_view(template_name="sucesso_contato.html"),name='sucesso'),
    path('pessoa/<int:id>', SalvarPessoa.as_view(),name='atualizar'),
    path('pessoa/insere', SalvarPessoa.as_view(), name='inserir'),
    path('listar', ListarPessoas.as_view(), name='listar_pessoas'),
]
