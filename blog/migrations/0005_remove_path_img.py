# Generated by Django 3.0 on 2021-05-09 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210507_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='path',
            name='img',
        ),
    ]