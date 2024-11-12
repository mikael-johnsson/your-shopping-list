from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import List, ListItem
from django.urls import reverse
from django.db.models import Max
from django.contrib import messages


def list_list(request):
    """
    View that renders the home page. If user is logged in the users lists
    are in the returned dictionary.
    List is a model that creates the users list.
    """
    if request.user.is_authenticated:
        queryset = List.objects.filter(author=request.user)
        lists = queryset

        return render(
            request,
            "list_app/list_list.html",
            {"lists": lists, }
            )
    else:
        return render(
            request,
            "list_app/list_list.html",
            )


def list_detail(request, id):
    """
    View that renders the detailed list view. In the list the user can
    see list items. Argument 'id' is the primary key of the list. It
    constructs the URL for list_detail.
    """
    if request.user.is_authenticated:
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
    Function that creates list for the user from the home page. It validates
    the name and contructs a new object of List. Redirects back to home page.
    """
    if request.user.is_authenticated:
        list = List()
        list.author = request.user
        list.name = request.POST.get('new-list-name')
        if list.name.isspace() != True:
            if len(list.name) <= 25:
                list.save()
                messages.success(request, "Your list is saved")
            else:
                messages.error(request, "Name can not be longer "
                                        "than 25 characters")
        else:
            messages.error(request, "Your list needs a real name")

        queryset = List.objects.filter(author=request.user)
        lists = queryset

        return redirect('home')

    else:
        return render(
            request,
            "403.html")


def edit_list_name(request, id):
    """
    View that updates the list name from the detailed list view.
    It validates the name and redirects to the detailed list view.
    """
    list = List.objects.get(id=id)
    items = ListItem.objects.all().filter(list=list.id)

    if request.user.is_authenticated:
        if request.method == "POST":
            list.name = request.POST.get('new-list-name')
            if list.name.isspace() != True:
                if len(list.name) <= 25:
                    list.save()
                    messages.success(request, "Your list is updated")
                else:
                    messages.error(request, "Name can not be longer "
                                        "than 25 characters")
            else:
                messages.error(request, "Your list needs a real name")

        return redirect('list_detail', id=id)
    else:
        return render(
               request,
               "403.html")


def list_delete(request, id):
    """
    View that deletes the list the user is displaying.
    Redirects back to home page.
    """
    if request.user.is_authenticated:
        queryset = List.objects.filter(author=request.user)
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
    
def clear_list(request, id):
    """
    View that deletes all items in the list the user is displaying.
    Redirects back to detailed list view.
    """
    if request.user.is_authenticated:
        list = List.objects.get(id=id)
        items = ListItem.objects.all().filter(list=list.id)

        if request.method == "POST":
            items.delete()
            messages.success(request, "You have cleared the list")

        return redirect('list_detail', id=id)
    else:
        return render(
               request,
               "403.html")


def create_item(request, id):
    """
    View to create ListItem. ListItem is a model with Foreing Key connecting
    it to a list. The view validates the content and fills out
    remaining fields (author and list). Redirects to detailed list view.
    """
    if request.user.is_authenticated:
        queryset = List.objects.filter(author=request.user)
        lists = queryset
        list = queryset.get(id=id)

        items = ListItem.objects.all().filter(list=id)

        if request.method == "POST":
            item = ListItem()
            item.author = request.user
            item.list = list
            item.content = request.POST.get("new-item")
            if item.content.isspace() != True:
                if len(item.content) <= 35:
                    item.save()
                    messages.success(request, "You have added item")
                else:
                    messages.error(request, "Item can not be longer "
                                            "than 35 characters")
            else:
                messages.error(request, "Your item need a real name")

        return redirect('list_detail', id=id)
    else:
        return render(
               request,
               "403.html")


def edit_item(request, id):
    """
    View to edit item content. Validates new item content and saves object.
    Redirects to detailed list view.
    """
    if request.user.is_authenticated:
        item = ListItem.objects.all().get(id=id)

        if request.method == "POST":
            item.content = request.POST.get("edit-item")
            if item.content.isspace() != True:
                if len(item.content) <= 35:
                    item.save()
                    messages.success(request, "You have updated item")
                else:
                    messages.error(request, "Item can not be longer than "
                                            "35 characters")
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
    View to delete item. Redirects to detailed list view.
    """
    if request.user.is_authenticated:
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
