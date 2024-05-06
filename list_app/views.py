from django.shortcuts import render
from django.views import generic
from .models import List, ListItem


# Create your views here.
class UsersLists(generic.ListView):
    queryset = List.objects.all()
    template_name = "list_app/list_list.html"




   