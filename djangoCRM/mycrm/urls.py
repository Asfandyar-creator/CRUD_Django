from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout_user'),
    path('register/', views.register_user, name='register'),
    path('customer-record/<int:pk>/', views.customer_record, name='record'),
    path('delete_record/<int:pk>/', views.delete_record, name='delete'),
    path('add_record/', views.add_record, name='add_record')
]