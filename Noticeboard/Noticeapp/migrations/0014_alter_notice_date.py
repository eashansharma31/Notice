# Generated by Django 4.1.7 on 2023-04-05 05:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Noticeapp', '0013_alter_notice_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 5, 11, 14, 17, 73487)),
        ),
    ]
