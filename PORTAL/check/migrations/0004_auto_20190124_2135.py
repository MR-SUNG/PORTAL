# Generated by Django 2.1.5 on 2019-01-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0003_auto_20190124_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]
