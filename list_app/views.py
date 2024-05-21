from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import List, ListItem
from django.urls import reverse
from django.db.models import Max


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
        return render(
            request,
            "list_app/list_list.html",
            )



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


def create_list(request, user):
    """
    """
    if(request.user.is_authenticated):
        list = List()
        list.author = request.user
        list.name = request.POST.get('new-list-name')
        list.save()

        queryset = List.objects.filter(author = request.user)
        lists = queryset

    return redirect('home')


def edit_list_name(request, id):

    list = List.objects.get(id=id)
    items = ListItem.objects.all().filter(list=list.id)

    if request.method == "POST":
        list.name = request.POST.get('new-list-name')
        list.save()
    
    return redirect('list_detail', id=id)


def list_delete(request, id):
    """
    view to delete list
    """
    queryset = List.objects.filter(author = request.user)
    lists = queryset
    list = queryset.filter(id=id)
    
    if request.method == "POST":
        list.delete()
    
    return render(
        request,
        "list_app/list_list.html",
        {"list": list,
        "lists": lists}
    )

def save_list(request, id):
    list = List.objects.get(id=id)
    dbItems = ListItem.objects.all().filter(list=id)
    
    

    
    
        
    
    return redirect('list_detail', id)

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
        item.content = request.POST.get("new-item")
        item.save()

    return redirect('list_detail', id=id)

def edit_item(request, id):
    """
    View to edit item when button clicked 
    """
    item = ListItem.objects.all().get(id=id)

    if request.method == "POST":
        item.content = request.POST.get("edit-item")
        item.save()

    list = item.list
    items = ListItem.objects.all().filter(list=list)

    return redirect('list_detail', id=list.id)

def delete_item(request, id):
    """
    View to delete item when button clicked
    """
    item = ListItem.objects.all().get(id=id)
    list = item.list
    items = ListItem.objects.all().filter(list=list)
    

    if request.method == "POST":
        item.delete()
    
    return redirect('list_detail', id=list.id)