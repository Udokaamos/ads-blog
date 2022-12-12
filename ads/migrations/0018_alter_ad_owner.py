# Generated by Django 4.0.7 on 2022-12-05 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0017_remove_ad_posts_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ad_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]