# Generated by Django 5.0.2 on 2024-02-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
