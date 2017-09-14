from django.contrib import admin
from django.db import models


# Create your models here.
class CrashLog(models.Model):
    """
    错误日志
    """
    log_id = models.CharField('ID', max_length=64)
    device_type = models.CharField('设备类型', max_length=32)
    package_name = models.CharField('包名', default='', max_length=64)
    version_name = models.CharField('版本名称', max_length=32)
    version_code = models.CharField('版本号', max_length=10)
    os_version_code = models.CharField('系统版本号', max_length=10)
    model_name = models.CharField('设备名称', max_length=32)
    net_state = models.CharField('网络状态', max_length=32)
    error_level = models.CharField('错误等级', max_length=32, default='ERROR')
    crash_log = models.TextField('错误日志')
    user_name = models.CharField('用户名', default='', max_length=64)
    report_time = models.DateTimeField('上传时间', auto_now_add=True)


class CrashLogAdmin(admin.ModelAdmin):
    list_display = ('log_id', 'device_type', 'version_code', 'model_name', 'os_version_code', 'report_time',)
    search_fields = ('os_version_code', 'user_name',)
    list_filter = ('device_type', 'version_code', 'model_name',)
    list_per_page = 25
