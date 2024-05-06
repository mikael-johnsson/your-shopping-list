from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import List, ListItem


# Create your views here.
class UsersLists(generic.ListView):
    queryset = List.objects.all()
    template_name = "list_app/list_list.html"

class ListItems(generic.ListView):
    queryset = ListItem.objects.all()
    template_name = "list_app/list_detail.html"


def list_detail(request, name):
    """
    Display and individual :model:`list_app.List`
    """
    #more of docstring...

    queryset = List.objects.all()
    list = get_object_or_404(queryset, name=name)
    items = ListItem.objects.all()
    

    return render(
        request,
        "list_app/list_detail.html",
        {"list": list,
        "items": items}
    )



   