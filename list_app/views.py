from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import List, ListItem
from django.urls import reverse


# Create your views here.
class UsersLists(generic.ListView):
    queryset = List.objects.all()
    template_name = "list_app/list_list.html" #create a list_list function inside?


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
    list = get_object_or_404(queryset, id=id)
    list.delete() #why doesn it delete?
    #add message to confirm deletion

    # return render(
    #     request,
    #     "list_app/list_detail.html",
    #     {"list": list} )

    return HttpResponseRedirect(reverse('list_list'))
   