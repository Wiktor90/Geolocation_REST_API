from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_set_up, name="api_set_up"),
    path('geodata-list/', views.geo_list, name='geo_list'),
    path('geodata-create/', views.geo_create, name='geo_create'),
    path('geodata-update/<int:pk>/', views.geo_update, name='geo_update'),
    path('geodata-details/<int:pk>/', views.geo_details, name='geo_details'),
    path('geodata-delete/<int:pk>/', views.geo_delete, name='geo_delete'),
]
