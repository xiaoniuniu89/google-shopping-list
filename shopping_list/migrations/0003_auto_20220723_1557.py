# Generated by Django 3.2 on 2022-07-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0002_shoppinglist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='shopping_list_items',
            field=models.ManyToManyField(blank=True, null=True, related_name='shopping_items', to='shopping_list.ShoppingListItem'),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='title',
            field=models.CharField(default='New List', max_length=128),
        ),
    ]
