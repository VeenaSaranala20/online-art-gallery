# Generated by Django 5.0 on 2024-03-09 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_alter_artwork_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(upload_to='artworks/'),
        ),
    ]
