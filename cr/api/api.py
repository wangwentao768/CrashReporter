import json
import uuid

import urllib3
from django.http import HttpResponse
from wxpy import *

from CrashReporter.settings import INNER_NET_URL, DINGDING_URL
from cr.models import CrashLog


def report_crash(request):
    request_params = request.POST
    device_type = request_params.get('deviceType')
    package_name = request_params.get('packageName')
    version_name = request_params.get('versionName')
    version_code = request_params.get('versionCode')
    os_version_code = request_params.get('osVersionCode')
    model_name = request_params.get('modelName')
    net_state = request_params.get('netState')
    error_level = request_params.get('errorLevel')
    username = request_params.get('userName')
    crash_log = request_params.get('crashLog')
    if crash_log is None:
        return HttpResponse('log can not be null')
    else:
        data = CrashLog()
        data.log_id = uuid.uuid1()
        data.device_type = device_type
        data.package_name = package_name
        data.version_name = version_name
        data.version_code = version_code
        data.os_version_code = os_version_code
        data.model_name = model_name
        data.net_state = net_state
        data.error_level = error_level
        data.user_name = username
        data.crash_log = crash_log
        data.save()
        title = '(' + data.deviceType + ')程序崩溃，点击链接查看详情:'
        url = 'http://' + INNER_NET_URL + ':8000/crashDetail?id=' + str(data.log_id)
        send_dingding_msg(title, url)
        return HttpResponse('crash log reported')


def send_wechat_msg(title, url):
    bot = Bot(cache_path=True, console_qr=True)
    # bot = Bot(cache_path=True)
    found = bot.groups().search(u'指尖鲨鱼测试')
    group = ensure_one(found)
    group.send_msg(title + url)


def send_dingding_msg(title, url):
    data = {
        'msgtype': 'link',
        'link': {
            'title': '请注意',
            'text': title,
            'picUrl': '',
            'messageUrl': url,
        }
    }
    http = urllib3.PoolManager()
    r = http.request('POST', DINGDING_URL, headers={'Content-Type': 'application/json'}, body=json.dumps(data))
    print(r.data)
