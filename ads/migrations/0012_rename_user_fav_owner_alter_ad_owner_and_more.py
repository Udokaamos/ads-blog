# Generated by Django 4.0.7 on 2022-11-30 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0011_alter_fav_unique_together_alter_ad_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fav',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='ad',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='fav',
            unique_together={('ad', 'owner')},
        ),
    ]