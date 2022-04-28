from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('linguagem/<int:linguagem_id>', views.linguagem, name='linguagem'),
    path('projeto/<int:projeto_id>', views.projeto, name='projeto')
]