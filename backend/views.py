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
    if request.method == "POST":
        req = json.loads(request.body)
        obj = CheckLocation()
        for k, v in req.items():
            setattr(obj, k, v)
        obj.create_at = datetime.datetime.now()
        obj.save()
        obj.refresh_from_db()
        return JsonResponse(obj.to_dict(), safe=False)

