# Generated by Django 4.2.11 on 2024-05-17 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list_app', '0004_remove_listitem_item_id_alter_list_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listitem',
            name='updated_on',
        ),
    ]