from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import List, ListItem
from django.urls import reverse
from django.db.models import Max
from django.contrib import messages


def list_list(request):
    if(request.user.is_authenticated):
        queryset = List.objects.filter(author = request.user)
        lists = queryset
        
        return render(
            request,
            "list_app/list_list.html",
            {"lists": lists,
            }
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
    if(request.user.is_authenticated):
        queryset = List.objects.all()
        list = get_object_or_404(queryset, id=id)
        items = ListItem.objects.all().filter(list=list.id)
        
        return render(
            request,
            "list_app/list_detail.html",
            {"list": list,
            "items": items}
        )
    else:
        return render(
            request, 
            "403.html")


def create_list(request, user):
    """
    """
    if(request.user.is_authenticated):
        list = List()
        list.author = request.user
        list.name = request.POST.get('new-list-name')
        if list.name.isspace() == False:
            if len(list.name) <= 25:
                list.save()
                messages.success(request, "Your list is saved")
            else:
                messages.error(request, "Name can not be longer than 25 characters")
        else: 
            messages.error(request, "You list needs a real name")

        queryset = List.objects.filter(author = request.user)
        lists = queryset

        return redirect('home')
    
    else:
        return render(
            request, 
            "403.html")


def edit_list_name(request, id):

    list = List.objects.get(id=id)
    items = ListItem.objects.all().filter(list=list.id)

    if(request.user.is_authenticated):
        if request.method == "POST":
            list.name = request.POST.get('new-list-name')
            if list.name.isspace() == False:
                if len(list.name) <= 25:
                    list.save()
                    messages.success(request, "Your list is updated")
            else:
                messages.error(request, "Name can not be longer than 25 characters")
            
        return redirect('list_detail', id=id)
    else: 
        return render(
        request, 
        "403.html")



def list_delete(request, id):
    """
    view to delete list
    """
    if(request.user.is_authenticated):
        queryset = List.objects.filter(author = request.user)
        lists = queryset
        list = queryset.filter(id=id)
        
        if request.method == "POST":
            list.delete()
            messages.success(request, "You have deleted list")
        
        return redirect('home')
    else: 
        return render(
        request, 
        "403.html")

def save_list(request, id):
    list = List.objects.get(id=id)
    items = ListItem.objects.all().filter(list=id)
    checkedItems = []
    unCheckedItems = []
    for item in items:
        if item.checked == True:
            checkedItems.append(item)
        else:
            unCheckedItems.append(item)
           
    
    return redirect('list_detail', id)

def create_item(request, id):
    """
    View to create item when add item button clicked
    """
    if(request.user.is_authenticated):
        queryset = List.objects.filter(author = request.user)
        lists = queryset
        list = queryset.get(id=id)

        items = ListItem.objects.all().filter(list=id)

        if request.method == "POST":
            item = ListItem()
            item.author = request.user
            item.list = list
            item.content = request.POST.get("new-item")
            if item.content.isspace() == False:
                if len(item.content) <= 35:
                    item.save()
                    messages.success(request, "You have added item")
                else:
                    messages.error(request, "Item can not be longer than 35 characters")
            else:
                messages.error(request, "Your item need a real name")
        
        return redirect('list_detail', id=id)
    else: 
        return render(
        request, 
        "403.html")

def edit_item(request, id):
    """
    View to edit item when button clicked 
    """
    if(request.user.is_authenticated):
        item = ListItem.objects.all().get(id=id)

        if request.method == "POST":
            item.content = request.POST.get("edit-item")
            if item.content.isspace() == False:
                if len(item.content) <= 35:
                    item.save()
                    messages.success(request, "You have updated item")
                else:
                    messages.error(request, "Item can not be longer than 35 characters")
            else:
                messages.error(request, "Your item need a real name")

        list = item.list
        items = ListItem.objects.all().filter(list=list)

        return redirect('list_detail', id=list.id)
    else: 
        return render(
        request, 
        "403.html")

def delete_item(request, id):
    """
    View to delete item when button clicked
    """
    if(request.user.is_authenticated):
        item = ListItem.objects.all().get(id=id)
        list = item.list
        items = ListItem.objects.all().filter(list=list)
        

        if request.method == "POST":
            item.delete()
            messages.success(request, "You have deleted item")
        
        return redirect('list_detail', id=list.id)
    else: 
        return render(
        request, 
        "403.html")