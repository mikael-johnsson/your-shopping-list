from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    """
    Model that creates a List object. List object is connected through foreign 
    key to Django User model. ListItem connects with List through foreign key.
    """
    name = models.CharField(max_length=25, default="New Shopping List")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="lists"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"Name of list: {self.name}"

class ListItem(models.Model):
    """
    Model that creates list items. ListItem object is connected through foreign 
    key to Django User model and List object.
    """
    list = models.ForeignKey(
        List, on_delete=models.CASCADE, related_name="list_items"
    )
    content = models.CharField(max_length=35)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="item_author"
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return f"Item: {self.content}"