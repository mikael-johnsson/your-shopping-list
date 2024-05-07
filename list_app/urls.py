from . import views
from django.urls import path


urlpatterns = [
    path('', views.list_list, name='home'),
    path('<int:id>/', views.list_detail, name='list_detail'),
    path('', views.list_list, name='list_delete'),
]