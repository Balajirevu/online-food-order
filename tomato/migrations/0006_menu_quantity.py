# Generated by Django 5.0.4 on 2024-06-12 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tomato', '0005_delete_addtocart'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]