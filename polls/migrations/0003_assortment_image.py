# Generated by Django 5.1.1 on 2024-11-25 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_assortment_delete_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='assortment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products_images/'),
        ),
    ]
