# Generated by Django 4.2.4 on 2023-08-28 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
