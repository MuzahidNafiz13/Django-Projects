# Generated by Django 5.0.6 on 2024-06-03 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0001_initial'),
        ('Posts', '0004_alter_posts_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]
