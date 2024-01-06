# Generated by Django 4.0.2 on 2024-01-03 10:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('texeclientapp', '0004_orders_delivery_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart_crm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=255, null=True)),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
                ('meterial', models.CharField(blank=True, max_length=255, null=True)),
                ('design', models.FileField(blank=True, null=True, upload_to='images/cart/design')),
                ('logo', models.FileField(blank=True, null=True, upload_to='images/cart/logos')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='texeclientapp.item')),
                ('model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='texeclientapp.sub_images')),
                ('sub_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='texeclientapp.sub_color')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.CharField(blank=True, max_length=250, null=True)),
                ('number', models.CharField(blank=True, max_length=250, null=True)),
                ('password', models.CharField(blank=True, max_length=250, null=True)),
                ('profile', models.ImageField(blank=True, default='static\\images\\static_image\\icon.svg', null=True, upload_to='images/propic')),
                ('joindate', models.DateField(default=datetime.date(2024, 1, 3), null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, default='active', max_length=255, null=True)),
                ('addres', models.TextField(blank=True, null=True)),
                ('role', models.CharField(blank=True, max_length=255, null=True)),
                ('dob', models.DateField(null=True)),
                ('location', models.CharField(blank=True, max_length=250, null=True)),
                ('otp', models.CharField(blank=True, max_length=250, null=True)),
                ('designation', models.CharField(blank=True, max_length=250, null=True)),
                ('complaint', models.CharField(blank=True, max_length=250, null=True)),
                ('orders', models.CharField(blank=True, max_length=250, null=True)),
                ('preformance', models.CharField(blank=True, max_length=250, null=True)),
                ('users_access', models.CharField(blank=True, max_length=250, null=True)),

            ],
        ),
        migrations.CreateModel(
            name='orders_crm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('total_amount', models.FloatField(blank=True, default=0, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('stage_count', models.IntegerField(blank=True, default=0, null=True)),
                ('stage', models.CharField(blank=True, max_length=255, null=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='texecrmapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='events_crm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='texecrmapp.orders_crm')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='texecrmapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='complaint_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(blank=True, max_length=255, null=True)),
                ('complaint', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('date_register', models.DateField(default=datetime.date(2024, 1, 3))),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('users', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='texecrmapp.users')),
            ],
        ),
        migrations.CreateModel(
            name='checkout_item_crm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=255, null=True)),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('item_price', models.FloatField(blank=True, null=True)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='texecrmapp.cart_crm')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='texeclientapp.item')),
                ('orders', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='texecrmapp.orders_crm')),
            ],
        ),
        migrations.AddField(
            model_name='cart_crm',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='texecrmapp.users'),
        ),
    ]
