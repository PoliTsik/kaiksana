# Generated by Django 5.0.2 on 2024-02-10 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='user_rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
