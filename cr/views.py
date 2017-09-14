from django.shortcuts import render

from CrashReporter.settings import INNER_NET_URL
from .models import CrashLog


# Create your views here.
def crash_detail(request):
    log_id = request.GET.get('id')
    log = CrashLog.objects.get(log_id=log_id)
    result = {
        'log': log,
        'innerUrl': 'http://' + INNER_NET_URL + ':8000/logList?deviceType=' + log.device_type
                    + '&versionCode=' + log.version_code
    }
    return render(request, 'crash_log.html', result)


def crash_list(request):
    request_params = request.GET
    device_type = request_params.get('deviceType')
    version_code = request_params.get('versionCode')
    data_list = CrashLog.objects.filter(deviceType=device_type, versionCode=version_code)
    result = {
        'logList': data_list,
        'innerUrl': 'http://' + INNER_NET_URL + ':8000/crashDetail?id='
    }
    return render(request, 'log_list.html', result)
