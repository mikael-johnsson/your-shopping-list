from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import List, ListItem
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.
# class UsersLists(generic.ListView):
#     queryset = List.objects.all()
#     template_name = "list_app/list_list.html" 

# def index(request):

#     return render(
#         request,
#         "list_app/index.html"
#         )

def list_list(request):
    queryset = List.objects.all()#adding filter author==request.user breaks the logout
    lists = queryset
    
    return render(
        request,
        "list_app/list_list.html",
        {"lists": lists,}
        )

#is this really needed?
#class ListItems(generic.ListView): 
    # queryset = ListItem.objects.all()
    # template_name = "list_app/list_detail.html"


def list_detail(request, id):
    """
    Display and individual :model:`list_app.List`
    """
    #more of docstring...

    queryset = List.objects.all()
    list = get_object_or_404(queryset, id=id)
    items = ListItem.objects.all().filter(list=list.id)
    

    return render(
        request,
        "list_app/list_detail.html",
        {"list": list,
        "items": items}
    )

def list_delete(request, id):
    """
    view to delete list
    """
    
    queryset = List.objects.all()
    list = queryset.filter(id=id)
    
    list.delete()
    #add modul to confirm deletion
  
    return HttpResponseRedirect(reverse('home'))
   