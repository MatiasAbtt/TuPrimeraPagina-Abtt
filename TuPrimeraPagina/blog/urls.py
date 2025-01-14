from django.urls import path
from . import views

urlpatterns = [
    path('crear_autor/', views.crear_autor, name='crear_autor'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear_post/', views.crear_post, name='crear_post'),
    path('buscar_posts/', views.buscar_posts, name='buscar_posts'),
]
