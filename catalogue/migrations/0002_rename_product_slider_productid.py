# Generated by Django 4.0 on 2021-12-26 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='product',
            new_name='productId',
        ),
    ]