# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 07:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrashLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_id', models.CharField(max_length=64, verbose_name='ID')),
                ('device_type', models.CharField(max_length=32, verbose_name='设备类型')),
                ('package_name', models.CharField(default='', max_length=64, verbose_name='包名')),
                ('version_name', models.CharField(max_length=32, verbose_name='版本名称')),
                ('version_code', models.CharField(max_length=10, verbose_name='版本号')),
                ('os_version_code', models.CharField(max_length=10, verbose_name='系统版本号')),
                ('model_name', models.CharField(max_length=32, verbose_name='设备名称')),
                ('net_state', models.CharField(max_length=32, verbose_name='网络状态')),
                ('error_level', models.CharField(default='ERROR', max_length=32, verbose_name='错误等级')),
                ('crash_log', models.TextField(verbose_name='错误日志')),
                ('user_name', models.CharField(default='', max_length=64, verbose_name='用户名')),
                ('report_time', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
            ],
        ),
    ]
