# Generated by Django 4.0.4 on 2022-05-25 01:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_alter_member_createdate_alter_member_updatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='createdate',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 5, 25, 10, 59, 37, 856136)),
        ),
        migrations.AlterField(
            model_name='member',
            name='updatedate',
            field=models.DateTimeField(blank=True, verbose_name=datetime.datetime(2022, 5, 25, 10, 59, 37, 856136)),
        ),
    ]