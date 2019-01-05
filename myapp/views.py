from django.http.response import HttpResponse
from django.shortcuts import render

from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

# Create your views here.
from .models import Dimension


def createDimension(request):
    print('create')
    obj = json.loads(request.body)
    dName = obj['dName']
    tID = obj['tID']
    try:
        dimension = Dimension(dName=dName, tID=tID)  # 填数据库时还要测评号tID，怎么拿到测评号tID呢？在这里先假设拿到了.
        dimension.save()
        result = {
            "code": 200,
        }
    except Exception as e:
        result = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(result), content_type="application/json")
