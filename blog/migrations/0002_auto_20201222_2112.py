# Generated by Django 2.2.5 on 2020-12-22 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='date_posted',
        ),
    ]
