from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
import json


@csrf_exempt
def count_down(request):
    if request.method == "PATCH":
        req = json.loads(request.body)
        time = CheckTime.objects.get(name=req['name']).to_dict()
        CheckTime.objects.filter(name=req['name']).update(time=time['time']+1, last_activity=datetime.datetime.now())
        model = [CheckTime.objects.filter(name=req['name']).first().to_dict_answer()]
        return JsonResponse(model, safe=False)


@csrf_exempt
def check_location(request):
    if request.method == "GET":
        name = int(request.GET.get('name', 0))
        longitude = int(request.GET.get('longitude', 0))
        width = int(request.GET.get('width', 0))
        width_window = int(request.GET.get('width_window', 0))
        country = int(request.GET.get('country', 0))
        city = int(request.GET.get('city', 0))
        region = int(request.GET.get('region', 0))
        timezone = int(request.GET.get('timezone', 0))
        obj = CheckLocation.objects.create(name=name, longitude=longitude, width=width, width_window=width_window,
                                           country=country, city=city, region=region, timezone=timezone,
                                           last_activity=datetime.datetime.now())
        return JsonResponse(obj.to_dict(), safe=False)

