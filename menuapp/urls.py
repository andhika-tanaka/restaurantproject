from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('new/', views.menu_add, name='menu_add'),
    path('<int:pk>/', views.menu_detail, name='menu_detail'),
    path('<int:pk>/edit', views.menu_edit, name='menu_edit'),
    path('<int:pk>/delete', views.menu_delete, name='menu_delete'),
]