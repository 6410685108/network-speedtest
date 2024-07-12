from django.shortcuts import render
import subprocess
import json
from .models import SpeedTestResult
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone

# def test_speed(request):
#     speedtest_output = subprocess.run(['speedtest', '--json'], capture_output=True, text=True)
#     if speedtest_output.returncode == 0:
#         try:
#             result = json.loads(speedtest_output.stdout)
#             download = result.get('download') / 1e6 if 'download' in result else None
#             upload = result.get('upload') / 1e6 if 'upload' in result else None
#             if download and upload:
#                 SpeedTestResult.objects.create(download_speed=download, upload_speed=upload)
#             results = SpeedTestResult.objects.order_by('-timestamp')
#             results_data = list(results.values('download_speed', 'upload_speed', 'timestamp'))
#             return render(request, 'home.html', {'result': result, 'results_data': json.dumps(results_data, cls=DjangoJSONEncoder)})
#         except json.JSONDecodeError as e:
#             return render(request, 'home.html', {'error': 'Failed to parse speedtest output.'})
#     else:
#         return render(request, 'home.html', {'error': 'Failed to run speedtest-cli.'})

def home(request):
    results = SpeedTestResult.objects.order_by('timestamp')
    results_data = list(results.values('download_speed', 'upload_speed', 'timestamp'))
    return render(request, 'home.html', {'results_data': json.dumps(results_data, cls=DjangoJSONEncoder)})

def test_internet_speed():
    speedtest_output = subprocess.run(['speedtest', '--json'], capture_output=True, text=True)
    if speedtest_output.returncode == 0:
        try:
            result = json.loads(speedtest_output.stdout)
            download = result.get('download') / 1e6 if 'download' in result else None
            upload = result.get('upload') / 1e6 if 'upload' in result else None
            print(download, upload, timezone.now())
            if download and upload:
                SpeedTestResult.objects.create(download_speed=download, upload_speed=upload)
        except json.JSONDecodeError as e:
            pass
    return