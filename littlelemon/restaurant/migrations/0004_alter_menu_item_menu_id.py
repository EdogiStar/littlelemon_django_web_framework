# Generated by Django 4.2.3 on 2023-07-24 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_menu_item_menu_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='menu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.menu'),
        ),
    ]