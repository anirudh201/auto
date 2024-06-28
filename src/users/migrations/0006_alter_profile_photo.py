# Generated by Django 4.0.5 on 2022-06-15 20:55

from django.db import migrations, models
import users.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to=users.utils.user_directory_path),
        ),
    ]