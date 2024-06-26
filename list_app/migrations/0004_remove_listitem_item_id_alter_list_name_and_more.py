# Generated by Django 4.2.11 on 2024-05-17 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list_app', '0003_listitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listitem',
            name='item_id',
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(default='New Shopping List', max_length=25),
        ),
        migrations.AlterField(
            model_name='listitem',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_items', to='list_app.list'),
        ),
    ]
