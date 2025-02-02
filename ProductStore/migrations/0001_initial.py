# Generated by Django 4.2.1 on 2023-05-31 05:56

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Special_Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_short_description', models.CharField(max_length=255)),
                ('actual_price', models.IntegerField()),
                ('list_price', models.IntegerField()),
                ('percent_off', models.IntegerField()),
                ('main_image_link', models.CharField(max_length=255)),
                ('sub_image_link_2', models.CharField(max_length=255)),
                ('sub_image_link_3', models.CharField(max_length=255)),
                ('sub_image_link_4', models.CharField(max_length=255)),
                ('product_long_description', tinymce.models.HTMLField()),
                ('product_specification', tinymce.models.HTMLField()),
                ('product_category', models.IntegerField(choices=[(1, 'Men Watch'), (2, 'Men Smart Watches'), (3, 'Men Rings'), (4, 'Men Wallet'), (5, 'Men Smart Wallet'), (6, 'Women Jewelry Sets'), (7, 'Women Fashion Watches'), (8, 'Women Fashion Rings'), (9, 'Women Fashion Necklace'), (10, 'Women Fashion Bags'), (11, 'Earbuds'), (12, 'USB Flash Drive')])),
                ('product_quantity', models.IntegerField()),
                ('slug_ref', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='product_name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Store_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_short_description', models.CharField(max_length=255)),
                ('actual_price', models.IntegerField()),
                ('list_price', models.IntegerField()),
                ('percent_off', models.IntegerField()),
                ('main_image_link', models.CharField(max_length=255)),
                ('sub_image_link_2', models.CharField(max_length=255)),
                ('sub_image_link_3', models.CharField(max_length=255)),
                ('sub_image_link_4', models.CharField(max_length=255)),
                ('product_long_description', tinymce.models.HTMLField()),
                ('product_specification', tinymce.models.HTMLField()),
                ('product_category', models.IntegerField(choices=[(1, 'Men Watch'), (2, 'Men Smart Watches'), (3, 'Men Rings'), (4, 'Men Wallet'), (5, 'Men Smart Wallet'), (6, 'Women Jewelry Sets'), (7, 'Women Fashion Watches'), (8, 'Women Fashion Rings'), (9, 'Women Fashion Necklace'), (10, 'Women Fashion Bags'), (11, 'Earbuds'), (12, 'USB Flash Drive')])),
                ('product_quantity', models.IntegerField()),
                ('slug_ref', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='product_name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Top_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_short_description', models.CharField(max_length=255)),
                ('actual_price', models.IntegerField()),
                ('list_price', models.IntegerField()),
                ('percent_off', models.IntegerField()),
                ('main_image_link', models.CharField(max_length=255)),
                ('sub_image_link_2', models.CharField(max_length=255)),
                ('sub_image_link_3', models.CharField(max_length=255)),
                ('sub_image_link_4', models.CharField(max_length=255)),
                ('product_long_description', tinymce.models.HTMLField()),
                ('product_specification', tinymce.models.HTMLField()),
                ('product_category', models.IntegerField(choices=[(1, 'Men Watch'), (2, 'Men Smart Watches'), (3, 'Men Rings'), (4, 'Men Wallet'), (5, 'Men Smart Wallet'), (6, 'Women Jewelry Sets'), (7, 'Women Fashion Watches'), (8, 'Women Fashion Rings'), (9, 'Women Fashion Necklace'), (10, 'Women Fashion Bags'), (11, 'Earbuds'), (12, 'USB Flash Drive')])),
                ('product_quantity', models.IntegerField()),
                ('slug_ref', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='product_name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='comment_images/')),
                ('rating', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
