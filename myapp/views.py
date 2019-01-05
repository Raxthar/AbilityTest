from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

from .models import ATest
# Create your views here.
def create(request):
    obj = json.loads(request.body)
    name = obj['title']
    describe = obj['describe']
    try:
        book = ATest(tName=name, tDescribe=describe)
        book.save()
        res = {
            "code": 200,
        }
    except Exception as e:
        res = {
            "code": 0,
            "errMsg": e
        }
    return HttpResponse(json.dumps(res), content_type="application/json")
