# Generated by Django 3.2 on 2022-07-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0003_auto_20220723_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='shopping_list_items',
            field=models.ManyToManyField(blank=True, related_name='shopping_items', to='shopping_list.ShoppingListItem'),
        ),
    ]
