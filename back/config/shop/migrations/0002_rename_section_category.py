# Generated by Django 4.0.5 on 2022-06-10 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Section',
            new_name='Category',
        ),
    ]
