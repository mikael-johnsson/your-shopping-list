from . import views
from django.urls import path


urlpatterns = [
    path('', views.list_list, name='home'),
    path('<int:id>/', views.list_detail, name='list_detail'),
    path('create/<str:user>/', views.create_list, name='create_list'),
    path('edit/<str:user>/', views.edit_list, name='edit_list'),
    path('delete/<int:id>/', views.list_delete, name='list_delete'),
    path('create_item/<int:id>/', views.create_item, name='create_item'),
    path('edit_item/<int:id>/', views.edit_item, name='edit_item'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item'),
]