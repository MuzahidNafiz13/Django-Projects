# Generated by Django 5.0.6 on 2024-06-07 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pcar',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='porder',
            name='car',
        ),
        migrations.RemoveField(
            model_name='porder',
            name='user',
        ),
        migrations.DeleteModel(
            name='PBrand',
        ),
        migrations.DeleteModel(
            name='PCar',
        ),
        migrations.DeleteModel(
            name='POrder',
        ),
    ]