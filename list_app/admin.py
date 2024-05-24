from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import List, ListItem

@admin.register(List)
class ListAdmin(SummernoteModelAdmin):
    list_display = ('name', 'author', 'created_on')
    search_fields = ['name']

admin.site.register(ListItem)
