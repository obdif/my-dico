# Generated by Django 4.1.4 on 2023-10-31 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mydico', '0002_customuser_delete_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
