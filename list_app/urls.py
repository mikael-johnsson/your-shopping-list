from . import views
from django.urls import path


urlpatterns = [
    path('', views.UsersLists.as_view(), name='home'),
]