# Generated by Django 2.1.5 on 2019-01-23 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_status',
            field=models.CharField(choices=[('finish', '완료'), ('ing', '진행'), ('pending', '보류')], default='ing', max_length=7),
        ),
        migrations.AlterField(
            model_name='post',
            name='kind',
            field=models.CharField(choices=[('first', '이슈공유'), ('second', '장애발생'), ('third', '이력관리'), ('fourth', '기타')], default='first', max_length=10),
        ),
    ]
