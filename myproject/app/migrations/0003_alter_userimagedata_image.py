# Generated by Django 4.1.6 on 2023-10-29 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_userimagedata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimagedata',
            name='image',
            field=models.ImageField(null=True, upload_to='media/images'),
        ),
    ]