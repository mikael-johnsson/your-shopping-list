from . import views
from django.urls import path


urlpatterns = [
    path('', views.list_list, name='home'),
    path('<int:id>/', views.list_detail, name='list_detail'),
    path('create/<str:user>/', views.create_list, name='create_list'),
    path('edit_list_name/<int:id>/', views.edit_list_name,
         name='edit_list_name'),
    path('delete/<int:id>/', views.list_delete, name='list_delete'),
    path('clear_list/<int:id>/', views.clear_list, name='clear_list'),
    path('create_item/<int:id>/', views.create_item, name='create_item'),
    path('edit_item/<int:id>/', views.edit_item, name='edit_item'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item'),
]
