# Generated by Django 5.0.4 on 2024-06-11 13:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tomato', '0002_alter_menu_menu_id_alter_order_order_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tomato.menu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tomato.new_user')),
            ],
        ),
    ]
