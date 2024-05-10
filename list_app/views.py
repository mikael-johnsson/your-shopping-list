from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import List, ListItem
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Max



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
        return render(
            request,
            "list_app/list_list.html",
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

def edit_list(request, user):
    
    user = List.objects.filter(author=request.user)
    maxid = user.aggregate(Max('id'))
    list = user.get(id=maxid["id__max"])
    items = ListItem.objects.all().filter(list=list.id)
    

    if request.method == "POST":
        print("nu är det post")
        list.name = request.POST.get('new-list-name')
        list.save()
    elif request.method == "GET":
        print("nu är det get")
    
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
    queryset = List.objects.filter(author = request.user)
    lists = queryset
    list = queryset.filter(id=id)
    
    if request.method == "POST":
        list.delete()
    else:
        print("The method isnt post :(")
    
  
    return render(
        request,
        "list_app/list_list.html",
        {"list": list,
        "lists": lists}
    )


def create_item(request, id):
    """
    View to create item when add item button clicked
    """
    queryset = List.objects.filter(author = request.user)
    lists = queryset
    list = queryset.get(id=id)

    items = ListItem.objects.all().filter(list=id)

    if request.method == "POST":
        item = ListItem()
        item.author = request.user
        item.list = list
        item.item_id = "1" #remove when deleted from model
        item.content = request.POST.get("new-item")
        item.save()
    else:
        print("nu blev det inte post i create_item")

    return render(
        request,
        "list_app/list_detail.html",
        {"list": list,
        "items": items,}
    )

def edit_item(request, id):
    """
    View to edit item when button clicked 
    """
    item = ListItem.objects.all().get(id=id)

    if request.method == "POST":
        item.content = request.POST.get("edit-item")
        item.save()
    else:
        print("No post request in edit_item ")

    list = item.list
    items = ListItem.objects.all().filter(list=list)

    return render(
        request,
        "list_app/list_detail.html",
        {"list": list,
        "items": items,}
    )

def delete_item(request, id):
    """
    View to delete item when button clicked
    """
    item = ListItem.objects.all().get(id=id)
    list = item.list
    items = ListItem.objects.all().filter(list=list)
    

    if request.method == "POST":
        item.delete()
    else:
        print("The method isnt post :(")
    
    return render(
        request,
        "list_app/list_detail.html",
        {"list": list,
        "items": items,}
    )