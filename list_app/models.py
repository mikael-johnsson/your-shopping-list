from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    #list_id = models.IntegerField()
    name = models.CharField(max_length=25, unique=True) #should or should not be unique?
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
    item_id = models.IntegerField()
    list = models.ForeignKey(
        List, on_delete=models.CASCADE, related_name="list_item"
    )
    content = models.CharField(max_length=35)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="item_author"
    )
    checked = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]