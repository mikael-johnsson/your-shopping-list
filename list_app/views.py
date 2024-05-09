from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import List, ListItem
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


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
    if(request.user.is_authenticated):
        queryset = List.objects.filter(author = request.user)
        lists = queryset
        
        return render(
            request,
            "list_app/list_list.html",
            {"lists": lists,}
            )
    else:
        #add message
        print("You are not logged in and can not see the lists")
        return HttpResponseRedirect(reverse('home'))

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

# create list here with default values, and edit values in different func when in list_detail
def create_list(request, user):
    """
    """

    list = List()
    list.author = request.user
    list.save()
    modalOkay = True

    if(request.user.is_authenticated):
        queryset = List.objects.filter(author = request.user)
        lists = queryset
    
    return render(
            request,
            "list_app/list_list.html",
            {"list": list,
            "lists": lists,
            "modalOkay": modalOkay}
            )

def edit_list(request):
    
    user = List.objects.filter(author=request.user)
    list = user.filter(name="New Shopping List") #change to filter on perhaps largest id
    list.name = request.POST
    print(request.POST)
    list.save()

    return render(
        request,
        "list_app/list_detail.html",
        {"list": list}
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
   