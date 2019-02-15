from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/edit/', views.prod_edit, name='prod_edit'),
    path('<int:pk>', views.prod_delete, name='prod_delete'),
]