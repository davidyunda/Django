# Generated by Django 4.0.3 on 2022-04-09 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel_wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='date_visited',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/'),
        ),
        migrations.AddField(
            model_name='place',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
