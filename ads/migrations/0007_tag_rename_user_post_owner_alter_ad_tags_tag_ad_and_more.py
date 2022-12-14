# Generated by Django 4.0.7 on 2022-11-28 14:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('ads', '0006_post_ad_posts_ad_tags_post_ad_post_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Title must be greater than 2 characters')])),
                ('text', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='ad',
            name='tags',
            field=models.ManyToManyField(related_name='owner_tags', through='ads.Tag', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tag',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.ad'),
        ),
        migrations.AddField(
            model_name='tag',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tag',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
