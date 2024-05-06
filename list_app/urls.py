from . import views
from django.urls import path


urlpatterns = [
    path('', views.UsersLists.as_view(), name='home'),
    path('<str:name>/', views.list_detail, name='list_detail'),
]