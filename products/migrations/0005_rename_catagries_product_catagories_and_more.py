# Generated by Django 4.2.17 on 2025-03-10 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_file_delete_mo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='catagries',
            new_name='catagories',
        ),
        migrations.AlterModelTable(
            name='catagory',
            table='catagoris',
        ),
    ]
